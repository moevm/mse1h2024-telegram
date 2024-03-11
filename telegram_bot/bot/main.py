import asyncio
import json
import os
from Messages.Messages import *
from telegram_bot.bot.Messages.MessageContent.TextContent import *
from telegram_bot.bot.Messages.MessageContent.Button import *

from telegram import ForceReply, Update, Bot, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from aio_pika import connect, abc


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(rf"Hi, {user.mention_html()}!", reply_markup=ForceReply(selective=True))


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await ButtonMessage(
        context,
        update,
        Text.Help(),
        keyboard_button=[[Button.Start()], [Button.Help()], [Button.ConfirmCommand()]]
    ).send()

# remove default table_name and table_url
async def confirm_notification(update: Update, context: ContextTypes.DEFAULT_TYPE, table_name: str = "Примеры таблиц", table_url: str = "https://docs.google.com/spreadsheets/d/1xM3ntz2wm62ESlbkFD_07Cbnta4ngwl8NhIAyrzbt2M/edit#gid=0") -> None:
    await ButtonMessage(
            context,
            update,
            FormatText.ConfirmNotification(table_name),
            markup_button=[[Button.ConfirmMessage()], [Button.Redirect(table_url)]]
        ).send()


async def mock(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


async def process_task(message: abc.AbstractIncomingMessage):
    async with message.process():
        task = json.loads(message.body.decode('utf-8'))
        await Bot(token=os.getenv("TELEGRAM_BOT_TOKEN")).send_message(chat_id=task['chat_id'], text=str(task))


async def control_queues():
    while True:
        try:
            connection = await connect(
                login=os.getenv('RABBITMQ_USER'),
                password=os.getenv('RABBITMQ_PASS'),
                host='rabbit')
            break
        except ConnectionError:
            print('Waiting for RabbitMQ connection')
            await asyncio.sleep(5)
    print('Successfully connected!')
    queue_name = "task_queue"
    channel = await connection.channel()
    queue = await channel.declare_queue(queue_name, auto_delete=True)
    await queue.consume(callback=process_task)
    try:
        # Wait until terminate
        await asyncio.Future()
    finally:
        await connection.close()


async def main() -> None:
    application = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("confirm", confirm_notification))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mock))

    async with application:
        await application.initialize()
        await application.start()
        task1 = asyncio.create_task(control_queues())
        task2 = asyncio.create_task(application.updater.start_polling())
        await asyncio.gather(task1, task2)


if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import datetime
import json
import os
import httpx
import logging

from .messages.text_converter import TextConverter
from .messages.messages_types import ButtonMessage, TextMessage
from .messages.text_content import FormatText, Text
from .messages.button import Button
from .task.answer_message import AnswerInterface
from .queue_manager.queue_manager import QueueManager

from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler

from aio_pika import abc

logger = logging.getLogger('MSE-telegram')
logger.setLevel(logging.DEBUG)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TELEGRAM_BOT_TOKEN)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(update.effective_user.id)
    logger.info(update.effective_chat.id)
    user = update.effective_user
    await client.post("http://backend:8000/api/users",
                      json={'username': f'{user.name}', "chat_id": f'{update.effective_chat.id}'})
    logger.info(update.effective_chat.id)
    await TextMessage(
        Text.START()
    ).send(context=context, update=update)


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await client.delete(f"http://backend:8000/api/users/{user.name}")
    await TextMessage(
        Text.STOP()
    ).send(context=context, update=update)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await ButtonMessage(
        Text.HELP(),
        keyboard_button=[[Button.Start(), Button.Help()]]
    ).send(context=context, update=update)


async def mock(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


async def process_task(message: abc.AbstractIncomingMessage):
    async with message.process():
        task = json.loads(message.body.decode('utf-8'))
        logger.info({"task receive": task})
        response = TextConverter.convert_markdown(task)

        if task["params"] and task["params"]["type"] == "confirm":
            table_name = task["params"]["table_name"]
            table_url = task["params"]["table_url"]
            table_hash = task["params"]["table_hash"]
            await ButtonMessage(
                response if response != "" else FormatText.NotificationTableTag(table_name, table_url),
                markup_button=[[Button.confirmMessage(table_hash), Button.redirect(table_url)]]
            ).send(bot=bot, _chat_id=int(task["chat_id"]))


async def query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query.data.split(" ")
    type = query[0] if len(query) > 0 else None
    table_hash = query[1] if len(query) > 1 else None

    logger.info(f"queue {str(query)}")

    if "confirm_notification" in type:
        answer = AnswerInterface(
            chat_id=str(update.effective_user.id),
            content="confirm the notification",
            params={
                "table_hash": table_hash,
                "chat_id": str(update.effective_user.id),
                "status": "CONFIRMED",
                "time": str(datetime.datetime.now())
            }
        )
        await QueueManager().add_answer_to_queue(answer)

    await update.callback_query.answer()


async def control_queues():
    await QueueManager().create_connection()
    await QueueManager().on_update_queue(process_task)

    try:
        # Wait until terminate
        await asyncio.Future()
    finally:
        await QueueManager().close()


async def main() -> None:
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("stop", stop))
    application.add_handler(CallbackQueryHandler(query_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mock))

    async with application:
        await application.initialize()
        await application.start()
        task1 = asyncio.create_task(control_queues())
        task2 = asyncio.create_task(application.updater.start_polling())
        await asyncio.gather(task1, task2)


if __name__ == "__main__":
    client = httpx.AsyncClient()
    logging.log(logging.INFO, "start bot")
    asyncio.run(main())

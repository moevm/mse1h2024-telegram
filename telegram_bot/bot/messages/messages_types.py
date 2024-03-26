from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext


class BaseMessage:
    def __init__(self, context: CallbackContext, update: Update):
        self.context = context
        self.update = update

    async def send(self):
        await self.context.bot.send_message(chat_id=self.update.effective_chat.id)


class TextMessage(BaseMessage):
    def __init__(self, context: CallbackContext, update: Update, text: str):
        super().__init__(context, update)
        self.text = text

    async def send(self):
        await self.context.bot.send_message(
            chat_id=self.update.effective_chat.id,
            text=self.text
        )


class ButtonMessage(TextMessage):
    def __init__(self,
                 context: CallbackContext,
                 update: Update,
                 text: str,
                 keyboard_button: list[list[KeyboardButton]] = None,
                 markup_button: list[list[InlineKeyboardButton]] = None
                 ):
        super().__init__(context, update, text)
        self.keyboard_button = keyboard_button
        self.markup_button = markup_button

    async def send(self):
        if self.keyboard_button is not None and self.markup_button is not None:
            raise Exception("Cannot use two panels of button at the same time")

        reply_markup = None
        if self.keyboard_button is not None:
            reply_markup = ReplyKeyboardMarkup(self.keyboard_button, one_time_keyboard=True, resize_keyboard=True)
        elif self.markup_button is not None:
            reply_markup = InlineKeyboardMarkup(self.markup_button)

        if reply_markup is None:
            await super().send()
        else:
            await self.context.bot.send_message(
                chat_id=self.update.effective_chat.id,
                text=self.text,
                reply_markup=reply_markup
            )

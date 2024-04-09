from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, Bot
from telegram.constants import ParseMode
from telegram.ext import ContextTypes


class BaseMessage:

    async def send(self, bot: Bot = None): pass

    async def send_to(self, chat_id: int): pass


class TextMessage(BaseMessage):
    def __init__(self, text: str):
        self.text = text

    async def send(self, bot: Bot = None,
                   context: ContextTypes.DEFAULT_TYPE = None,
                   update: Update = None,
                   _chat_id: int = None):

        if bot is None and context is None:
            raise Exception("No enough parameters to send message")
        sender_bot = bot if bot else context.bot

        if _chat_id is None and update is None:
            raise Exception("No enough parameters to define chat id")
        chat_id = _chat_id if _chat_id else update.effective_chat.id

        await sender_bot.send_message(
            chat_id=chat_id,
            text=self.text,
            parse_mode=ParseMode.MARKDOWN_V2,
        )


class ButtonMessage(TextMessage):
    def __init__(self,
                 text: str,
                 keyboard_button: list[list[KeyboardButton]] = None,
                 markup_button: list[list[InlineKeyboardButton]] = None,
                 ):
        super().__init__(text)
        self.keyboard_button = keyboard_button
        self.markup_button = markup_button

    def create_buttons(self):
        if self.keyboard_button is not None and self.markup_button is not None:
            raise Exception("Cannot use two panels of button at the same time")

        reply_markup = None
        if self.keyboard_button is not None:
            reply_markup = ReplyKeyboardMarkup(self.keyboard_button, one_time_keyboard=True, resize_keyboard=True)
        elif self.markup_button is not None:
            reply_markup = InlineKeyboardMarkup(self.markup_button)

        return reply_markup

    async def send(self, bot: Bot = None,
                   context: ContextTypes.DEFAULT_TYPE = None,
                   update: Update = None,
                   _chat_id: int = None):

        if bot is None and context is None:
            raise Exception("No enough parameters to send message")
        sender_bot = bot if bot else context.bot

        if _chat_id is None and update is None:
            raise Exception("No enough parameters to define chat id")
        chat_id = _chat_id if _chat_id else update.effective_chat.id

        reply_markup = self.create_buttons()
        if reply_markup is None:
            await super().send()
        else:
            await sender_bot.send_message(
                chat_id=chat_id,
                text=self.text,
                reply_markup=reply_markup,
                parse_mode=ParseMode.MARKDOWN_V2,
            )

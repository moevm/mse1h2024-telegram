from enum import Enum

from telegram import InlineKeyboardButton, KeyboardButton


class Button(Enum):
    Help = KeyboardButton("/help")
    Start = KeyboardButton("/start")
    ConfirmCommand = KeyboardButton("/confirm")

    # example of button with url
    @classmethod
    def redirect(cls, url: str) -> InlineKeyboardButton:
        return InlineKeyboardButton("Таблица", url=url, callback_data="table_redirect")

    @classmethod
    def confirm_message(cls, table_hash: str) -> InlineKeyboardButton:
        return InlineKeyboardButton("Подтвердить✅", callback_data=f"confirm_notification {table_hash}")

    def __call__(self):
        return self.value

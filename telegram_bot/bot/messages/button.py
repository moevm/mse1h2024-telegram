from enum import Enum

from telegram import InlineKeyboardButton, KeyboardButton


class Button(Enum):
    # simple button
    ConfirmMessage = InlineKeyboardButton("Подтвердить✅", callback_data="confirm_notification")
    Help = KeyboardButton("/help")
    Start = KeyboardButton("/start")
    ConfirmCommand = KeyboardButton("/confirm")

    # example of button with url
    @classmethod
    def Redirect(cls, url: str) -> InlineKeyboardButton:
        return InlineKeyboardButton("Таблица", url=url, callback_data="table_redirect")

    def __call__(self):
        return self.value

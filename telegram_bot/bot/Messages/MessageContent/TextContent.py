from enum import Enum


class Text(Enum):
    Greeting = "Привет! Я помогаю получать уведоления об изменениях в таблицах ЛЭТИ"
    Help = "Это бот ЛЭТИ. Пока что я знаю команды /start, /help и /confirm."

    def __call__(self):
        return self.value


class FormatText(Enum):
    ConfirmNotification = "Вы получили это сообщение, так как вас упомянули в таблице \"{}\""

    def __call__(self, *args):
        return self.value.format(*args)

from enum import Enum


class Text(Enum):
    START = r"*Привет\!* Я помогаю получать уведоления об изменениях в таблицах *ЛЭТИ*"
    HELP = r"Это бот *ЛЭТИ*\. Доступные команды */start* и */help*"
    STOP = r"*Вы отписались от уведомлений\!*"

    def __call__(self):
        return self.value


class FormatText(Enum):
    NotificationTableTag = "Вы получили это сообщение, так как вас упомянули в [{}]({})"

    def __call__(self, *args):
        return self.value.format(*args)

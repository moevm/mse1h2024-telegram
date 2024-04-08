from enum import Enum


class Text(Enum):
    Start = "*Привет\!* Я помогаю получать уведоления об изменениях в таблицах *ЛЭТИ*"
    Help = "Это бот *ЛЭТИ*\. Доступные команды */start* и */help*"
    Stop = "*Вы отписались от уведомлений\!*"

    def __call__(self):
        return self.value


class FormatText(Enum):
    ConfirmNotification = "Вы получили это сообщение, так как вас упомянули в [{}]({})"

    def __call__(self, *args):
        return self.value.format(*args)

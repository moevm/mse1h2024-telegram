from pydantic import BaseModel
from typing import Dict


class TaskInterface(BaseModel):
    content: str | None = None
    params: Dict[str, str] = {}


class TaskTelegramMessage(TaskInterface):
    chat_id: str

    @classmethod
    def create_telegram_message(cls, chat_id: str, content: str, params: Dict[str, str]):
        return TaskTelegramMessage(chat_id=chat_id, content=content, params=params)

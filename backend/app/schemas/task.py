from pydantic import BaseModel
from typing import Dict


class TaskInterface(BaseModel):
    content: str | None = None
    params: Dict[str, str] = {}


class TaskTelegramMessage(TaskInterface):
    chat_id: str

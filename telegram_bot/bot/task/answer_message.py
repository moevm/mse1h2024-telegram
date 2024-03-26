from pydantic import BaseModel
from typing import Dict


class AnswerInterface(BaseModel):
    content: str | None = None
    params: Dict[str, str] = {}


class AnswerConfirmMessage(AnswerInterface):
    chat_id: str

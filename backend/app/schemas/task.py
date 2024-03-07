import uuid
from typing import Dict

from pydantic import BaseModel


class SampleTask(BaseModel):
    chat_id: str
    content: str | None = None
    params: Dict[str, str] = {}

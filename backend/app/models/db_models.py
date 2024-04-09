from typing import List, Optional
from enum import Enum
from datetime import datetime
from beanie import Document
from pydantic import Field, BaseModel
from beanie.odm.fields import Indexed


class Status(str, Enum): 
    sended = "SENDED"
    confirmed = "CONFIRMED"
    error = "ERROR"


class Level(str, Enum):
    error = "ERROR"
    info = "INFO"
    debug = "DEBUG"


class Provider(str, Enum):
    google = "GOOGLE"


class Page(BaseModel):
    id: str  # uuid
    page_id: str
    teacher_column: str
    column1: str
    column2: str
    comparison_operator: str
    notification_text: str


class Table(Document):
    name: str
    table_id: str
    provider: Provider
    update_frequency: int
    pages: Optional[List[Page]]

    class Settings:
        name = "table"


class Teacher(Document):
    namesList: List[str]
    telegram_login: str

    class Settings:
        name = "teacher"


class Log(Document):
    date: datetime
    level: Level
    text: str

    class Settings:
        name = "log"


class Statistic(Document):
    hash: Indexed(str, unique=True)
    status: Status

    class Settings:
        name = "statistic"


class TelegramUser(Document):
    username: str
    chat_id: str

    class Settings:
        name = "tguser"
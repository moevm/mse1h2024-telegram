from typing import List, Optional
from enum import Enum
from datetime import datetime
from beanie import Document
from pydantic import BaseModel
from beanie import Indexed


class Status(str, Enum):
    SENDED = "SENDED"
    CONFIRMED = "CONFIRMED"
    ERROR = "ERROR"


class Level(str, Enum):
    ERROR = "ERROR"
    INFO = "INFO"
    DEBUG = "DEBUG"


class Provider(str, Enum):
    GOOGLE = "GOOGLE"


class Page(BaseModel):
    id: str  # uuid
    name: str
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
    names_list: List[str]
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
    table_link: str
    table_name: str
    teacher: str
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None

    class Settings:
        name = "statistic"


class TelegramUser(Document):
    username: str
    chat_id: str

    class Settings:
        name = "tguser"

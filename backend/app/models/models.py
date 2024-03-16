from typing import Optional, List
from enum import Enum
from datetime import datetime
from beanie import Document, PydanticObjectId, Link
from pydantic import Field, BaseModel

class Role(str, Enum):
    admin = "ADMIN"
    teacher = "TEACHER"

class Level(str, Enum):
    error = "ERROR"
    info = "INFO"
    debug = "DEBUG"

class Provider(str, Enum):
    google = "GOOGLE"
    yandex = "YANDEX"

class Page(BaseModel):
    name: str
    teacher_column: str
    columns: List[str]
    rule: str
    notification_text: str

class Table(Document):
    name: str
    link: str
    provider: Provider
    update_frequency: int
    pages: List[Page]

    class Settings:
        name="table"

class Teacher(Document):
    name: str
    patronymic: str
    surname: str
    telegram_login: str
    role: Role

    class Settings:
        name = "teacher"

class Log(Document):
    date: datetime
    level: Level
    text: str

    class Settings:
        name = "log"
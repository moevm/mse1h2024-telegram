from pydantic import BaseModel
from logging import LogRecord, Handler
from datetime import datetime
import asyncio
from ..models.db_models import Log
from ..core.socket import sio


def log_save_callback(task: asyncio.Task[Log]) -> None:
    log = task.result()
    asyncio.create_task(sio.emit("log", log.model_dump_json()))


class DatabaseHandler(Handler):
    def __init__(self, level: int | str = 0) -> None:
        super().__init__(level)

    def emit(self, record: LogRecord) -> None:
        time = datetime.strptime(record.asctime, "%d-%m-%Y %H:%M:%S")
        log = Log(level=record.levelname, date=time, text=record.getMessage())
        asyncio.create_task(log.create()).add_done_callback(log_save_callback)


class LogConfig(BaseModel):
    LOGGER_NAME: str = "MSE-telegram"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    version: int = 1
    disable_existing_loggers: bool = False
    formatters: dict = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
    }
    handlers: dict = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "database": {
            "()": "app.config.log_config.DatabaseHandler"
        }
    }
    loggers: dict = {
        LOGGER_NAME: {"handlers": ["default", "database"], "level": LOG_LEVEL},
    }

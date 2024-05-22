from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from logging.config import dictConfig
import logging

from .callback.ConfirmCallback import process_update
from .queue.queue_manager import QueueManager
from .config.log_config import LogConfig
from .routers import ping, auth, add_sample_task, crud
from .tables.tables_manager import TablesManager
from .models.db_models import Table
from .database import init_db
from .config.settings import settings
from .core.socket import sio_app


dictConfig(LogConfig().dict())
logger = logging.getLogger('MSE-telegram')


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db(str(settings.mongo_db_uri), settings.MONGO_INITDB_DATABASE)
    await QueueManager().create_connection()
    await QueueManager().on_update_queue(process_update)
    await restore_data()
    logger.info('Сервер запущен')
    yield
    TablesManager().shutdown()

app = FastAPI(
    root_path=settings.API_STR,
    lifespan=lifespan
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(ping.router)
app.include_router(auth.router)
app.include_router(add_sample_task.router)
app.include_router(crud.router)

app.mount("/", sio_app)


async def restore_data():
    TablesManager().add_tables(*(await Table.find_all().to_list()))

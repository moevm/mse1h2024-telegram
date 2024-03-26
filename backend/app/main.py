import asyncio
import json
import os
from aio_pika import abc
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from logging.config import dictConfig
import logging

from .queue.queue_manager import QueueManager
from .routers import ping, auth, add_sample_task
from .config.log_config import LogConfig
from .schemas.task import TaskTelegramMessage
from .routers import ping, auth, add_sample_task, crud
from .tables import tables_manager
from .database import init_db
from .config.settings import settings

dictConfig(LogConfig().dict())
logger = logging.getLogger('MSE-telegram')

app = FastAPI()
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


@app.on_event('startup')
async def startup_event():
    logger.info('Server started')
    await init_db(str(settings.MONGO_DB_URI), settings.MONGO_DB)
    await QueueManager().create_connection()

    # example of filling queue with tasks
    for i in range(10):
        await asyncio.sleep(1)
        task = TaskTelegramMessage(chat_id="560639281", content=f"hello {i}", params={"1": "1", "2": "2"})
        await QueueManager().add_task_to_queue(task)

    # example subscribe to queue
    await QueueManager().on_update_queue(process_update)


# example callback for receive answer
async def process_update(message: abc.AbstractIncomingMessage):
    async with message.process():
        update = json.loads(message.body.decode('utf-8'))
        logger.info({"answer from bot receive": update})

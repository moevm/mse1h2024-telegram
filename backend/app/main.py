import asyncio
import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .queue.task_manager import QueueManager
from .routers import ping, auth, add_sample_task

from logging.config import dictConfig
import logging
from .config.log_config import LogConfig
from .schemas.task import TaskTelegramMessage

from aio_pika import abc

dictConfig(LogConfig().dict())
logger = logging.getLogger('MSE-telegram')

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:8080",
        "http://frontend",
        "http://frontend:8080"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(ping.router)
app.include_router(auth.router)
app.include_router(add_sample_task.router)


@app.on_event('startup')
async def startup_event():
    logger.info('Server started')

    # example of filling queue with tasks
    for i in range(10):
        await asyncio.sleep(1)
        logger.info(i)
        task = TaskTelegramMessage(chat_id="560639281", content=f"hello {i}", params={"1": "1", "2": "2"})
        logger.info(f"{i} 1")
        await QueueManager().create_connection()  # can be used as singleton
        logger.info(f"{i} 2")
        await QueueManager().add_task_to_queue(task)
        logger.info(f"{i} 3")

    # example subscribe to queue
    manager = await QueueManager().create_connection() # can be used as singleton
    await manager.on_update_queue(process_update)


# example callback for receive
async def process_update(message: abc.AbstractIncomingMessage):
    async with message.process():
        update = json.loads(message.body.decode('utf-8'))
        logging.info({"update receive": update})

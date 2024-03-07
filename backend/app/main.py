from fastapi import FastAPI
from .routers import ping, add_sample_task

from logging.config import dictConfig
import logging
from .config.log_config import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger('MSE-telegram')

app = FastAPI()
app.include_router(ping.router)
app.include_router(add_sample_task.router)


@app.on_event('startup')
async def startup_event():
    logger.info('Server started')

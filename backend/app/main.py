from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import ping, auth, add_sample_task
import os

from logging.config import dictConfig
import logging
from .config.log_config import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger('MSE-telegram')

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        str(origin).strip("/") for origin in os.getenv("BACKEND_CORS_ORIGINS")
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

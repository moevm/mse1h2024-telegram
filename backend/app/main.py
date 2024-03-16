from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import ping, auth, add_sample_task, crud

from logging.config import dictConfig
import logging
from .config.log_config import LogConfig
from database import init_db

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
app.include_router(crud.router)

@app.on_event('startup')
async def startup_event():
    logger.info('Server started')
    await init_db("mongodb://localhost:27017/bot_db", "bot_db")

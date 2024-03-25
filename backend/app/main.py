from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import ping, auth, add_sample_task, crud
from .tables import tables_manager
from logging.config import dictConfig
import logging
from .config.log_config import LogConfig
from .config.settings import settings
from .database import init_db

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
app.include_router(crud.router)


@app.on_event('startup')
async def startup_event():
    logger.info('Server started')
    await init_db(str(settings.MONGO_DB_URI), settings.MONGO_DB)
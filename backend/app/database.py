from beanie import init_beanie
import motor.motor_asyncio
from .models.db_models import Table, Teacher, Log, TelegramUser, Statistic


async def init_db(address: str, name: str):
    client = motor.motor_asyncio.AsyncIOMotorClient(address)
    await init_beanie(database=client[name], document_models=[Teacher, Log, Table, TelegramUser, Statistic])
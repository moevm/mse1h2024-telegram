import logging
import json
from aio_pika import abc
from datetime import datetime

from ..models.db_models import Status, Statistic

logger = logging.getLogger('MSE-telegram')


async def process_update(message: abc.AbstractIncomingMessage):
    async with message.process():
        update = json.loads(message.body.decode('utf-8'))
        logger.info(f"Уведомление было подтверждено: {update}")
        await confirm_statistic(update["params"]["table_hash"])


async def confirm_statistic(table_hash: str):
    statistic = await Statistic.find_one(Statistic.hash == table_hash)
    if statistic:
        statistic.status = Status.CONFIRMED
        statistic.updated_at = datetime.now()
        await statistic.save()

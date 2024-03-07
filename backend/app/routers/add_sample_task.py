import uuid
import os

from aio_pika import connect, Message
from fastapi import APIRouter
from ..schemas.task import SampleTask

router = APIRouter(
    tags=["add_sample_task"],
    responses={200: {"description": "Successful Response"}},
)


async def add_task_to_queue(task: SampleTask):
    connection = await connect(
        login=os.getenv('RABBITMQ_USER'),
        password=os.getenv('RABBITMQ_PASS'),
        host='rabbit')
    channel = await connection.channel()
    await channel.default_exchange.publish(Message(
        str(task.json()).encode()), routing_key='task_queue')
    await connection.close()


@router.post("/add_sample_task")
async def add_sample_task(task: SampleTask):
    await add_task_to_queue(task)
    return {'result': f'Task for {task.chat_id} chat added to queue'}

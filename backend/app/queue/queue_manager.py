import logging
import os
import asyncio
from aio_pika import connect, Message
from ..schemas.task import TaskInterface


class QueueManager(object):
    __instance = None
    __connection = None
    __channel = None
    logger = logging.getLogger('MSE-telegram')

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.__instance = super(QueueManager, cls).__new__(cls)
        return cls.__instance

    async def create_connection(self):
        if self.__connection is None:
            while True:
                try:
                    self.__connection = await connect(
                        login=os.getenv('RABBITMQ_USER'),
                        password=os.getenv('RABBITMQ_PASS'),
                        host='rabbit')
                    break
                except ConnectionError:
                    print('Waiting for RabbitMQ connection')
                    await asyncio.sleep(5)

        if self.__channel is None:
            self.__channel = await self.__connection.channel()

        self.logger.info("connection created")

    async def add_task_to_queue(self, task: TaskInterface, routing_key: str = 'task_queue') -> None:
        if self.__channel is None:
            await self.create_connection()
        await self.__channel.default_exchange.publish(Message(
            str(task.json()).encode()), routing_key=routing_key)

    async def on_update_queue(self, callback, routing_key: str = 'answer_queue'):
        if self.__channel is None:
            await self.create_connection()

        queue = await self.__channel.declare_queue(routing_key, auto_delete=True)
        await queue.consume(callback=callback)

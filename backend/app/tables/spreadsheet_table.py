import asyncio
import logging
from collections import defaultdict

from .table_interface import InterfaceTable
from ..queue.queue_manager import QueueManager
from ..schemas.task import TaskTelegramMessage
from ..models.db_models import TelegramUser
from . import get_client

dateformat = '%d.%m.%Y %H:%M:%S'
logger = logging.getLogger('MSE-telegram')

google_link_format = 'https://docs.google.com/spreadsheets/d/{table_id}/edit#gid={page_id}&range={row}:{row}'


class SpreadsheetTable(InterfaceTable):

    def __init__(self, table_ref) -> None:
        self.__id = table_ref.table_id
        self.__timer = table_ref.update_frequency
        self.tmp_hashes = defaultdict(int)  # TODO: move hashes from local temporary variable to a database
        self.worksheets = table_ref.pages

    def log(self, info):
        logger.info(info)

    async def __parse_record(self, worksheet, record, i: int):
        new_hash = hash(str(record))
        # TODO: condition parser should be created as a different manager,
        #  that will determine the necessity of notification
        notify = new_hash != self.tmp_hashes[i]
        self.tmp_hashes[i] = new_hash
        # self.log(str((new_hash, record, await TelegramUser.find_all().to_list())))
        if notify:
            # TODO: for now notifications are passed to any user, will be fixed later
            for user in await TelegramUser.find_all().to_list():
                await QueueManager().add_task_to_queue(TaskTelegramMessage.create_telegram_message(
                    chat_id=user.chat_id,
                    content=f'Произошло изменение в таблице. Требуется проверка. '
                            f'{google_link_format.format(table_id=self.__id, page_id=worksheet.page_id, row=i + 2)}',
                    params={}
                ))

    async def pull(self) -> None:
        while True:
            await asyncio.sleep(self.__timer)
            client = await get_client()
            ss = await client.open_by_key(self.__id)
            for worksheet in self.worksheets:
                wks = await ss.get_worksheet_by_id(int(worksheet.page_id))
                records = await wks.get_all_records()
                self.log(str(records))
                for i, record in enumerate(records):
                    await self.__parse_record(worksheet, record, i)

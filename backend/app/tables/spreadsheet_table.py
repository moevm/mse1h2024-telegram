import asyncio
import logging
from collections import defaultdict

from gspread.exceptions import InvalidInputValue
from gspread.utils import column_letter_to_index

from .comparator.ComparatorHandler import ComparatorHandler
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

    async def notify_users(self, records, worksheet):
        try:
            notified_users_names, rows_changed = ComparatorHandler().compare_record(
                records,
                column_letter_to_index(worksheet.teacher_column) - 1,
                column_letter_to_index(worksheet.column1) - 1,
                column_letter_to_index(worksheet.column2) - 1,
                worksheet.comparison_operator,
                self.tmp_hashes)
        except InvalidInputValue:
            raise Exception('Invalid input found in provided columns')

        telegram_subscribers = await TelegramUser.find_all().to_list()
        notified_users_chat_id = []
        notified_users_row = []

        for index, subscriber in enumerate(telegram_subscribers):
            if subscriber.username in notified_users_names:
                notified_users_chat_id.append(subscriber.chat_id)
                notified_users_row.append(rows_changed[index])

        for index, chat_id in enumerate(notified_users_chat_id):
            table_link = google_link_format.format(
                table_id=self.__id,
                page_id=worksheet.id,
                row=notified_users_row[index] + 2)

            await QueueManager().add_task_to_queue(TaskTelegramMessage(
                chat_id=chat_id,
                params={"type": "confirm",
                        "table_name": "MSE",
                        "table_url": table_link}))

    async def pull(self) -> None:
        while True:
            await asyncio.sleep(self.__timer)
            client = await get_client()
            ss = await client.open_by_key(self.__id)
            for worksheet in self.worksheets:
                wks = await ss.worksheet(worksheet.name)
                records = await wks.get_all_values()
                await self.notify_users(records, worksheet)

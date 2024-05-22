import asyncio
import logging
from collections import defaultdict

from gspread.exceptions import InvalidInputValue
from gspread.utils import column_letter_to_index

from .comparator.ComparatorHandler import ComparatorHandler
from .table_interface import InterfaceTable
from ..queue.queue_manager import QueueManager
from ..schemas.task import TaskTelegramMessage
from ..models.db_models import Teacher, TelegramUser
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
            teacher_rows = ComparatorHandler().compare_records(
                records,
                column_letter_to_index(worksheet.teacher_column) - 1,
                column_letter_to_index(worksheet.column1) - 1,
                column_letter_to_index(worksheet.column2) - 1,
                worksheet.comparison_operator,
                self.tmp_hashes)
        except InvalidInputValue:
            logger.error('Неккоректное значение в столбцах')
            raise Exception('Invalid input found in provided columns')

        teachers = await Teacher.find_all().to_list()
        telegram_subscribers = await TelegramUser.find_all().to_list()
        telegram_subscribers_dict = defaultdict(set)

        for teacher in teachers:
            for pseudo in teacher.names_list:
                if pseudo in teacher_rows:
                    telegram_subscribers_dict[teacher.telegram_login] |= teacher_rows[pseudo]

        for subscriber in telegram_subscribers:
            if subscriber.username in telegram_subscribers_dict:
                for row in telegram_subscribers_dict[subscriber.username]:
                    await self.send_notification(worksheet.id, subscriber.chat_id, row)

    async def send_notification(self, page_id, chat_id, row_index):
        table_link = google_link_format.format(
            table_id=self.__id,
            page_id=page_id,
            row=row_index + 1)

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

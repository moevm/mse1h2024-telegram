import asyncio
import logging
from datetime import datetime

from ..table_interface import InterfaceTable
from . import get_client

dateformat = '%d.%m.%Y %H:%M:%S'
logger = logging.getLogger('MSE-telegram')

class Table(InterfaceTable):

    def __init__(self, timer: int) -> None:
        self.id = '1'
        self.__url = "https://docs.google.com/spreadsheets/d/1qhzjptVXAf_lDg3gJogGVguCDSzBoBlLDFPN2W2K8bQ/edit#gid=2015026419"
        self.__timer = timer
        self.worksheets = [{
            'title': 'Ответы на форму (1)',
            'rules': {
                'first': 'Дата последней отправки',
                'second': 'Дата проверки'
            },
            'teacher': 'Преподаватель',
        }]
        self.__teacher_map = {
            'Иванов И.И.': 'ivanov',
            'Петров П.П.': 'petrov',
            'Семенов С.С.': 'semen'
        }


    def log(self, row: int, title: str, teacher: str):
        logger.info(
            {
                'table': self.__url,
                'worksheet': title,
                'row': row+1,
                'to': teacher
            }
        )


    def __parse_record(self, worksheet, record, i: int):
        rules = worksheet['rules']
        try:
            first_check_column = record[rules['first']]
            second_check_column = record[rules['second']]
            teacher = record[worksheet['teacher']]

            if len(second_check_column) == 0:
                self.log(i+1, worksheet['title'], self.__teacher_map[teacher])
                return

            first_timestamp = datetime.strptime(first_check_column, dateformat)
            second_timestamp = datetime.strptime(second_check_column, dateformat)

            if second_timestamp >= first_timestamp:
                return

            self.log(i+1, worksheet['title'], self.__teacher_map[teacher])
        except Exception as e:
            logger.error(f"Catch error: {e}")
    

    async def pull(self) -> None:
        while True:
            await asyncio.sleep(self.__timer)
            client = await get_client()
            ss = await client.open_by_url(self.__url)
            for worksheet in self.worksheets:
                wks = await ss.worksheet(worksheet['title'])
                records = await wks.get_all_records()
                for i, record in enumerate(records):
                    self.__parse_record(worksheet, record, i)
                    
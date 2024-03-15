import asyncio
import pygsheets
import logging
from datetime import datetime
dateformat = '%d.%m.%Y %H:%M:%S'
logger = logging.getLogger('MSE-telegram')
gc = pygsheets.authorize(service_account_env_var= 'GDRIVE_API_CREDENTIALS')

class Table():
    def __init__(self) -> None:
        self.id = '1'
        self.__url = "https://docs.google.com/spreadsheets/d/1qhzjptVXAf_lDg3gJogGVguCDSzBoBlLDFPN2W2K8bQ/edit#gid=2015026419"
        self.__timer = 10
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

    async def pull(self) -> None:
        while True:
            await asyncio.sleep(self.__timer)
            ss = gc.open_by_url(self.__url)
            for worksheet in self.worksheets:
                wks = ss.worksheet_by_title(worksheet['title'])
                records = wks.get_all_records()
                rules = worksheet['rules']
                for i, record in enumerate(records):
                    try:
                        first_check_column = record[rules['first']]
                        second_check_column = record[rules['second']]
                        teacher = record[worksheet['teacher']]
                        if len(second_check_column) == 0:
                            logger.info({
                                'table': self.__url,
                                'worksheet': worksheet['title'],
                                'row': i+1,
                                'to': self.__teacher_map[teacher]
                            })
                            continue
                        first_timestamp = datetime.strptime(first_check_column, dateformat)
                        second_timestamp = datetime.strptime(second_check_column, dateformat)
                        if second_timestamp >= first_timestamp:
                            continue
                        logger.info({
                                'table': self.__url,
                                'worksheet': worksheet['title'],
                                'row': i+1,
                                'to': self.__teacher_map[teacher]
                            })
                    except Exception as e:
                        logger.error(f"Catch error: {e}")


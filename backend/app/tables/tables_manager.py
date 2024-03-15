import asyncio
from .table import Table

class TablesManager():
    __tables = {}
    __event_loop = None
    def __init__(self) -> None:
        self.__event_loop = asyncio.get_event_loop()


    def add_table(self, table: Table) -> None:
        task = self.__event_loop.create_task(table.pull())
        self.__tables[table.id] = task

table = Table()
tables_manager = TablesManager()
tables_manager.add_table(table)
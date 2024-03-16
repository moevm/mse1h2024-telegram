import asyncio
from .table_interface import InterfaceTable
from .gsheets.table import Table
from typing import Dict

class TablesManager():
    """
    Tables Manager help's to control tables
    """
    __tables: Dict[str, asyncio.Task] = {}
    __event_loop = None
    def __init__(self) -> None:
        self.__event_loop = asyncio.get_event_loop()


    def add_table(self, table: InterfaceTable) -> None:
        """
        Add table to event loop
        """
        task = self.__event_loop.create_task(table.pull())
        self.__tables[table.id] = task

    def delete_table(self, table_id: str):
        """
        Remove table from event loop
        """
        task = self.__tables.pop(table_id)
        if task:
            task.cancel()

# TODO: Delete delete with lines
table = Table()
tables_manager = TablesManager()
tables_manager.add_table(table)
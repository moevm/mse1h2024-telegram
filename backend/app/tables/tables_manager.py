import asyncio
from typing import Dict
from ..models.db_models import Table
from .spreadsheet_table import SpreadsheetTable


class TablesManager:
    """
    Tables Manager help's to control tables
    """
    __instance = None
    __tables: Dict[str, asyncio.Task] = {}

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.__instance = super(TablesManager, cls).__new__(cls)
        return cls.__instance

    def add_tables(self, *tables):
        for table in tables:
            self.add_table(table)

    def add_table(self, table: Table) -> None:
        """
        Add table to event loop
        """
        if table.table_id in self.__tables:
            self.delete_table(table.table_id)
        sp = SpreadsheetTable(table)
        task = asyncio.create_task(sp.pull())
        self.__tables[table.table_id] = task

    def update_table(self, table: Table) -> None:
        """
        Add table to event loop
        """
        self.delete_table(table.table_id)
        self.add_table(table)

    def delete_table(self, table_id: str):
        """
        Remove table from event loop
        """
        task = self.__tables.pop(table_id)
        if task:
            task.cancel()

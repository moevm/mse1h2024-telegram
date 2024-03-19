import asyncio
from .table_interface import InterfaceTable
from .gsheets.table import Table
from typing import Dict, Tuple

class TablesManager():
    """
    Tables Manager help's to control tables
    """
    __tables: Dict[str, asyncio.Task] = {}


    def add_table(self, *tables: Tuple[InterfaceTable, ...]) -> None:
        """
        Add table to event loop
        """
        for table in tables:
            task = asyncio.create_task(table.pull())
            self.__tables[table.id] = task

    def delete_table(self, table_id: str):
        """
        Remove table from event loop
        """
        task = self.__tables.pop(table_id)
        if task:
            task.cancel()

# TODO: Delete delete with lines

tables = [Table(i) for i in range(5, 100, 5)]
tables_manager = TablesManager()
tables_manager.add_table(*tables)
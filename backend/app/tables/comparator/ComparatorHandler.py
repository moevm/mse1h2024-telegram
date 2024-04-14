import json
import logging
from typing import TypeVar
from .Operator import Operator
T = TypeVar('T')


class ComparatorHandler:

    def compare_record(self, records, teacher, columns, rule, tmp_hashes) -> [str]:
        notified_users = []
        rows_changed = []
        logging.getLogger('MSE-telegram').info(f"hashes {str(tmp_hashes)}")

        for row, record in enumerate(records):
            new_hash = hash(str(record))
            logging.getLogger('MSE-telegram').info(f"new hash for record {record} {new_hash}")
            notify = new_hash != tmp_hashes[row]
            logging.getLogger('MSE-telegram').info(f"notify {notify}")
            if notify:
                tmp_hashes[row] = new_hash
                logging.getLogger('MSE-telegram').info(f"hashe changed")
                logging.getLogger('MSE-telegram').info(f"columns {columns[0]} - {record[columns[0]]} {columns[1]} - {record[columns[1]]}")

                if self.compare_row(record[columns[0]], record[columns[1]], Operator.get(rule)):
                    logging.getLogger('MSE-telegram').info(f"compare {record[columns[0]]} {rule} {record[columns[1]]} true")

                    notified_users.append(record[teacher])
                    rows_changed.append(row)
                logging.getLogger('MSE-telegram').info(f"notify end")

        return notified_users, rows_changed

    # def compare_table(self, ids: [int], left_column: [str], right_column: [str], operator_symbol: str) -> [int]:
    #     operator = Operator[operator_symbol]
    #
    #     return [chat_id for chat_id in ids]
    #
    # def compare_columns(self, left_column: List[T], right_column: List[T], operator: Operator) -> [bool]:
    #     if len(left_column) != len(right_column):
    #         raise Exception("Columns are not the same size")
    #
    #     return [
    #         self.compare_row(left_column[index], right_column[index], operator)
    #         for index in range(len(left_column))
    #     ]

    def compare_row(self, left_value: str, right_value: str, operator: Operator):
        logging.getLogger('MSE-telegram').info(f"compare {left_value} {right_value}")
        return operator.compare(left_value, right_value)

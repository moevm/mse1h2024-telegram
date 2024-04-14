from typing import TypeVar, List
from .Operator import Operator

T = TypeVar('T')


class ComparatorHandler:

    def compare_record(self, record) -> [int]:
        # parse record
        return self.compare_table(ids, left_column, right_column, operator)

    def compare_table(self, ids: [int], left_column: [str], right_column: [str], operator_symbol: str) -> [int]:
        operator = Operator[operator_symbol]

        return [chat_id for chat_id in ids]

    def compare_columns(self, left_column: List[T], right_column: List[T], operator: Operator) -> [bool]:
        if len(left_column) != len(right_column):
            raise Exception("Columns are not the same size")

        return [
            self.compare_row(left_column[index], right_column[index], operator)
            for index in range(len(left_column))
        ]

    def compare_row(self, left_value: str, right_value: str, operator: Operator):
        return operator.compare(left_value, right_value)

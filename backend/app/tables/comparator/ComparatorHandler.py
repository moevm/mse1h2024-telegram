from collections import defaultdict
import datetime

from .Operator import Operator


class ComparatorHandler:

    def compare_records(self, records, teacher, column1, column2, rule, tmp_hashes) -> [str]:
        teacher_row_dict = defaultdict(set)

        for row, record in enumerate(records):
            new_hash = hash(str(record))
            notify = new_hash != tmp_hashes[row]
            if notify:
                tmp_hashes[row] = new_hash
                if self.compare_row(record[column1], record[column2], Operator.get(rule)):
                    teacher_row_dict[record[teacher]].add(row)

        return teacher_row_dict

    def compare_columns(self, left_column: [], right_column: [], operator: Operator) -> [bool]:
        if len(left_column) != len(right_column):
            raise Exception("Columns are not the same size")

        return [
            self.compare_row(left_column[index], right_column[index], operator)
            for index in range(len(left_column))
        ]

    def compare_row(self, left_value: str, right_value: str, operator: Operator):
        a, b = self.values_convert(left_value, right_value)
        return operator.compare(a, b)

    def values_convert(self, value1, value2):
        try:
            return float(value1), float(value2)
        except Exception:
            pass

        try:
            return self.convert_date(value1), self.convert_date(value2)
        except Exception:
            pass

        return str(value1), str(value2)

    def convert_date(self, value):
        try:
            return datetime.datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            pass

        try:
            return datetime.datetime.strptime(value, '%d.%m.%Y %H:%M:%S')
        except ValueError:
            pass

        return value
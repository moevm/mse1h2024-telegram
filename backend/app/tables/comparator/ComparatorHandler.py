from .Operator import Operator


class ComparatorHandler:

    def compare_record(self, records, teacher, columns, rule, tmp_hashes) -> [str]:
        notified_users = []
        rows_changed = []

        for row, record in enumerate(records):
            new_hash = hash(str(record))
            notify = new_hash != tmp_hashes[row]
            if notify:
                tmp_hashes[row] = new_hash

                if self.compare_row(record[columns[0]], record[columns[1]], Operator.get(rule)):
                    notified_users.append(record[teacher])
                    rows_changed.append(row)

        return notified_users, rows_changed

    def compare_columns(self, left_column: [], right_column: [], operator: Operator) -> [bool]:
        if len(left_column) != len(right_column):
            raise Exception("Columns are not the same size")

        return [
            self.compare_row(left_column[index], right_column[index], operator)
            for index in range(len(left_column))
        ]

    def compare_row(self, left_value: str, right_value: str, operator: Operator):
        return operator.compare(left_value, right_value)

import logging
from enum import Enum
from abc import ABC


class Comparator(ABC):
    def compare(self, left_value, right_value) -> bool: pass


class Operator(Enum):
    EQ = Comparator()
    NEQ = Comparator()
    GT = Comparator()
    LT = Comparator()
    GE = Comparator()
    LE = Comparator()

    @staticmethod
    def get(key):
        match key:
            case "==": return Operator.EQ
            case "!=": return Operator.NEQ
            case ">": return Operator.GT
            case "<": return Operator.LT
            case ">=": return Operator.GE
            case "<=": return Operator.LE
            case _: raise Exception("Undefined compare operator symbol")

    def compare(self, left_value, right_value) -> bool:
        logging.getLogger('MSE-telegram').info("Compare in comparator")
        logging.getLogger('MSE-telegram').info(f"type of {type(left_value)} type of {type(right_value)}")
        match self:
            case Operator.EQ: return left_value == right_value
            case Operator.NEQ: return left_value != right_value
            case Operator.GT: return left_value > right_value
            case Operator.LT: return left_value < right_value
            case Operator.GE: return left_value >= right_value
            case Operator.LE: return left_value <= right_value

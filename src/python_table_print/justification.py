from enum import Enum

from .table_exception import TableException


class Justification(Enum):
    """An enum used for justifying text in the table"""

    LEFT = 0
    CENTRE = 1
    RIGHT = 2


class UnknownJustification(TableException):
    pass

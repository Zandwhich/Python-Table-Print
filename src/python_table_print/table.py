from enum import Enum
from math import ceil, floor
from typing import Sequence


BASE_BORDER = "*"


# TODO: You finished with implementing the logic for the right/left/centre justification printing out
#       And then see if you can clean up the code more, specifically breaking it down into smaller functinos
#       And then do more tests for that
#       And then do more doco in code
#       And then do more examples with the new code you just wrote
#       And then update the README
#       And then get rid of the develop branch? (Is it overkill for this project?)


class Justification(Enum):
    """An enum used for justifying text in the table"""

    RIGHT = 0
    CENTRE = 1
    LEFT = 2


class _Cell:
    """The basic building block of the table that stores the text and the justification of itself"""

    def __init__(self, text: str, justification: Justification | None = None) -> None:
        self.justification: Justification | None = justification
        self.text = text

    def get_cell_as_string(self, max_length: int, border_character: str) -> str:
        # Edge case if there is nothing for this column
        if max_length == 0:
            return " " + border_character

        if self.justification == None or self.justification == Justification.RIGHT:
            return (
                " " * (max_length - len(self.text) + 1)
                + self.text
                + " "
                + border_character
            )

        if self.justification == Justification.LEFT:
            return (
                " "
                + self.text
                + (" " * (max_length - len(self.text) + 1))
                + border_character
            )

        if self.justification == Justification.CENTRE:
            return (
                " " * (floor((max_length - len(self.text)) / 2) + 1)
                + self.text
                + " " * (ceil((max_length - len(self.text)) / 2) + 1)
                + border_character
            )

        # TODO: Raise a "Justification not implemented" exception
        else:
            raise Exception


class _Column:
    """An abstraction of the column of the table, which holds information about the column"""

    def __init__(self) -> None:
        self.max_length = 0


class _Row:
    """An abstraction of the row of the table, which holds each of the cells in that row of the table"""

    def __init__(self, *row: str, justification: Justification | None = None) -> None:
        self.cells: dict[int, _Cell] = {}

        for i in range(0, len(row)):
            self.cells[i] = _Cell(row[i], justification)

    def set_justification_for_cells(self, justification: Justification | None) -> None:
        for cell in self.cells.values():
            cell.justification = justification

    def get_row_as_string(
        self, border_character: str, max_lengths: Sequence[int]
    ) -> str:
        final_row = border_character

        for i in range(0, len(max_lengths)):
            if i < len(self.cells):
                final_row += self.cells[i].get_cell_as_string(
                    max_lengths[i], border_character
                )

            else:
                final_row += " " * (max_lengths[i] + 2) + border_character

        return final_row + "\n"


class PrintTable:
    def __init__(self) -> None:
        self.has_header_row: bool = True
        self._columns: dict[int, _Column] = {}
        self._rows: dict[int, _Row] = {}
        self._border_character = BASE_BORDER

    def _check_and_increase_max_column_length(self, column_i: int, length: int) -> None:
        """Takes in the column number and the length of the new string at that column and changes the length to the given length if longer, or if that column doesn't yet exist.

        Args:
            column (int): The column at which this is ocurring
            length (int): The length of the new string
        """
        # If there is no column for this yet, add one
        if column_i >= len(self._columns):
            self._columns[column_i] = _Column()
            self._columns[column_i].max_length = length
            return

        # Check if this length is longer than the currently stored one. If so, update
        if length > self._columns[column_i].max_length:
            self._columns[column_i].max_length = length

    def _total_border_length(self) -> int:
        """Figures out the length of the table

        Returns:
            int: The length of the table
        """
        total_border_length = 0

        for col_len in self._columns.values():
            total_border_length += (
                col_len.max_length + 3 if not col_len.max_length == 0 else 2
            )

        return total_border_length + 1

    def _get_border_row(self) -> str:
        return BASE_BORDER * self._total_border_length() + "\n"

    def _get_header(self, row: _Row, border_character: str) -> str:
        return self._get_row(row, border_character) + self._get_border_row()

    def _get_row(self, row: _Row, border_character: str) -> str:
        return row.get_row_as_string(
            border_character, [column.max_length for column in self._columns.values()]
        )

    def add_row(self, *row: str) -> None:
        for col_i in range(0, len(row)):
            self._check_and_increase_max_column_length(col_i, len(row[col_i]))

        self._rows[len(self._rows)] = _Row(*row)

    def set_table_justification(self, justification: Justification) -> None:
        for row in self._rows.values():
            row.set_justification_for_cells(justification)

    def set_row_justification(self, row_i: int, justification: Justification) -> None:
        self._rows[row_i].set_justification_for_cells(justification)

    def set_cell_justification(
        self, row_i: int, column_i: int, justificaiton: Justification
    ) -> None:
        self._rows[row_i].cells[column_i].justification = justificaiton

    def get_table(self) -> str:
        if len(self._rows) == 0:
            # TODO: Throw a "table has no length" exception
            raise Exception

        table = self._get_border_row()

        if self.has_header_row:
            table += self._get_header(self._rows[0], self._border_character)

        for i in range(1 if self.has_header_row else 0, len(self._rows)):
            table += self._get_row(self._rows[i], self._border_character)

        return table + self._get_border_row()

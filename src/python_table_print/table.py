from enum import Enum
from math import ceil, floor
from typing import Sequence


BASE_BORDER = "*"


# TODO:
#       * See if you can clean up the code more, specifically breaking it down into smaller functions
#       * Do more examples with the new code you just wrote
#       * Update the README
#       * Get rid of the develop branch? (Is it overkill for this project?)


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
        """Returns the cell in string format with the correct formatting.

        Args:
            max_length (int): The max length of a cell in that column.
            border_character (str): The character to be used on the border at the sides

        Raises:
            Exception: If there is an incorrect/unsupported justification

        Returns:
            str: The cell as a string with the correct justicication in place
        """
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
        """Sets the justification for all of the cells in the row

        Args:
            justification (Justification | None): The justification to set the cells to. If `None` is passed in, it sets the justificaiton to the default,
            which currently is the right justification.
        """
        for cell in self.cells.values():
            cell.justification = justification

    def get_row_as_string(
        self, border_character: str, max_lengths: Sequence[int]
    ) -> str:
        """Returns the row as a string

        Args:
            border_character (str): The border character that is being used for the table
            max_lengths (Sequence[int]): The max lengths for all of the columns

        Returns:
            str: _description_
        """
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
    """The table itself. More documentation to come!"""

    def __init__(self) -> None:
        self.has_header_row: bool = True

        # TODO: Is a dictionary whose keys are ints essentially a list in Python?
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
        """Creates the 'border row', or the top and botom row of the table made up of only border characters

        Returns:
            str: The border row made up of only border characters
        """
        return BASE_BORDER * self._total_border_length() + "\n"

    def _get_header(self, row: _Row, border_character: str) -> str:
        """Creates the 'header rows', which is the row of text sandwiched between two border rows

        Args:
            row (_Row): The row of text to sandwich between the border rows
            border_character (str): The border character

        Returns:
            str: The row of text sandwiched between two border rows
        """
        return (
            row.get_row_as_string(
                border_character,
                [column.max_length for column in self._columns.values()],
            )
            + self._get_border_row()
        )

    def add_row(self, *row: str) -> None:
        """Adds another row to the bottom of the table

        Args:
            row (*str): The next row of text to be added to the table
        """
        for col_i in range(0, len(row)):
            self._check_and_increase_max_column_length(col_i, len(row[col_i]))

        self._rows[len(self._rows)] = _Row(*row)

    def set_table_justification(self, justification: Justification) -> None:
        """Sets the justification for the whole table. Overrides any previous justification that was set

        Args:
            justification (Justification): The justification for the table
        """
        for row in self._rows.values():
            row.set_justification_for_cells(justification)

    def set_row_justification(self, row_i: int, justification: Justification) -> None:
        """Sets the justification for the row in the table. Overrides any previous justification for that row that was set.

        Args:
            row_i (int): The row to justify.
            justification (Justification): The justification for the row
        """
        self._rows[row_i].set_justification_for_cells(justification)

    def set_column_justification(
        self, col_i: int, justification: Justification
    ) -> None:
        """Sets the justificatoin for the column in the table. Overrides any previous justification for that row that was set.

        Args:
            col_i (int): The index of the column to change
            justification (Justification): The justification to set for the cells in that column
        """
        for row_i in range(0, len(self._rows)):
            self.set_cell_justification(row_i, col_i, justification)

    def set_cell_justification(
        self, row_i: int, column_i: int, justificaiton: Justification
    ) -> None:
        """Sets the justification for a specific cell in the table. Overrides any previous justification for that cell that was set.

        Args:
            row_i (int): The row that the cell is in.
            column_i (int): The column that the cell is in.
            justificaiton (Justification): The justification for the cell.
        """
        self._rows[row_i].cells[column_i].justification = justificaiton

    def get_table(self) -> str:
        """Returns the current table as a string

        Raises:
            Exception: If there is no data, throws an exception. TODO: Create the actual exception for this.

        Returns:
            str: The currenct table
        """
        if len(self._rows) == 0:
            # TODO: Throw a "table has no length" exception
            raise Exception

        table = self._get_border_row()

        if self.has_header_row:
            table += self._get_header(self._rows[0], self._border_character)

        for i in range(1 if self.has_header_row else 0, len(self._rows)):
            table += self._rows[i].get_row_as_string(
                self._border_character,
                [column.max_length for column in self._columns.values()],
            )

        return table + self._get_border_row()

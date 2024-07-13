from math import ceil, floor
from .justification import Justification
from .column import Column
from .row import Row


BASE_BORDER = "*"

# Table Characters
TABLE_CHARACTER_HORIZONTAL_BAR = "─"
TABLE_CHARACTER_VERTICAL_BAR = "│"

TABLE_CHARACTER_TOP_LEFT = "┌"
TABLE_CHARACTER_TOP_RIGHT = "┐"
TABLE_CHARACTER_TOP_SEPARATOR = "┬"

TABLE_CHARACTER_BOTTOM_LEFT = "└"
TABLE_CHARACTER_BOTTOM_RIGHT = "┘"
TABLE_CHARACTER_BOTTOM_SEPARATOR = "┴"

TABLE_CHARACTER_MIDDLE_LEFT_SEPARATOR = "├"
TABLE_CHARACTER_MIDDLE_RIGHT_SEPARATOR = "┤"
TABLE_CHARACTER_MIDDLE_SEPARATOR = "┼"


class PrintTable:
    """The table itself. More documentation to come!"""

    def __init__(self) -> None:
        self.has_header_row: bool = True

        # TODO: Is a dictionary whose keys are ints essentially a list in Python?
        self._columns: dict[int, Column] = {}
        self._rows: dict[int, Row] = {}
        self._title: str | None = None
        self._title_justification: Justification = Justification.CENTRE

    def _border(self, left_char: str, right_char: str, separator_char: str) -> str:
        border = left_char

        for column in self._columns.values():
            border += (
                TABLE_CHARACTER_HORIZONTAL_BAR
                * (column.max_length + 2 if column.max_length > 0 else 1)
                + separator_char
            )

        return border[:-1] + right_char + "\n"

    def _top_border(self) -> str:
        return self._border(
            TABLE_CHARACTER_TOP_LEFT,
            TABLE_CHARACTER_TOP_RIGHT,
            TABLE_CHARACTER_TOP_SEPARATOR,
        )

    def _bottom_border(self) -> str:
        return self._border(
            TABLE_CHARACTER_BOTTOM_LEFT,
            TABLE_CHARACTER_BOTTOM_RIGHT,
            TABLE_CHARACTER_BOTTOM_SEPARATOR,
        )

    def _middle_border(self) -> str:
        return self._border(
            TABLE_CHARACTER_MIDDLE_LEFT_SEPARATOR,
            TABLE_CHARACTER_MIDDLE_RIGHT_SEPARATOR,
            TABLE_CHARACTER_MIDDLE_SEPARATOR,
        )

    def _check_and_increase_max_column_length(self, column_i: int, length: int) -> None:
        """Takes in the column number and the length of the new string at that column and changes the length to the given length if longer, or if that column doesn't yet exist.

        Args:
            column (int): The column at which this is ocurring
            length (int): The length of the new string
        """
        # If there is no column for this yet, add one
        if column_i >= len(self._columns):
            self._columns[column_i] = Column()
            self._columns[column_i].max_length = length
            return

        # Check if this length is longer than the currently stored one. If so, update
        if length > self._columns[column_i].max_length:
            self._columns[column_i].max_length = length

    def _total_border_length(self) -> int:
        """Figures out the length of the table, including the two border characters themselves

        Returns:
            int: The length of the table
        """
        total_border_length = 0

        for col_len in self._columns.values():
            total_border_length += (
                col_len.max_length + 3 if not col_len.max_length == 0 else 2
            )

        return total_border_length + 1

    def _get_header(self, row: Row) -> str:
        """Creates the 'header rows', which is the row of text sandwiched between two border rows

        Args:
            row (_Row): The row of text to sandwich between the border rows
            border_character (str): The border character

        Returns:
            str: The row of text sandwiched between two border rows
        """
        return (
            row.get_row_as_string(
                TABLE_CHARACTER_VERTICAL_BAR,
                [column.max_length for column in self._columns.values()],
            )
            + self._middle_border()
        )

    def _get_title_row(self) -> str:
        """Creates the title row for the table if the title is set. Otherwise returns just the top border row

        NOTE: For now, we will cut off the title if it's too long. This will be fixed in GitHub Issue #61
        TODO: Address the above

        Args:
            border_character (str): The border character

        Returns:
            str: The title of the table, or an empty string if the title is not set
        """

        if not self._title:
            return self._top_border()

        # We want to cut off the title (for now) to not go passed the length of the table
        title = self._title[: self._total_border_length() - 4]

        length_without_borders = self._total_border_length() - 4

        match self._title_justification:
            case Justification.LEFT:
                title = (
                    TABLE_CHARACTER_VERTICAL_BAR
                    + " "
                    + title
                    + (" " * (length_without_borders - len(title) + 1))
                    + TABLE_CHARACTER_VERTICAL_BAR
                    + "\n"
                )

            case Justification.CENTRE:
                title = (
                    TABLE_CHARACTER_VERTICAL_BAR
                    + " " * (floor((length_without_borders - len(title)) / 2) + 1)
                    + title
                    + " " * (ceil((length_without_borders - len(title)) / 2) + 1)
                    + TABLE_CHARACTER_VERTICAL_BAR
                    + "\n"
                )

            case Justification.RIGHT:
                title = (
                    TABLE_CHARACTER_VERTICAL_BAR
                    + " " * (length_without_borders - len(title) + 1)
                    + title
                    + " "
                    + TABLE_CHARACTER_VERTICAL_BAR
                    + "\n"
                )

            case _:
                # TODO: Raise "Unsupported Justification" Exception
                raise Exception()

        return (
            self._border(
                TABLE_CHARACTER_TOP_LEFT,
                TABLE_CHARACTER_TOP_RIGHT,
                TABLE_CHARACTER_HORIZONTAL_BAR,
            )
            + title
            + self._border(
                TABLE_CHARACTER_MIDDLE_LEFT_SEPARATOR,
                TABLE_CHARACTER_MIDDLE_RIGHT_SEPARATOR,
                TABLE_CHARACTER_TOP_SEPARATOR,
            )
        )

    def add_row(self, *row: str) -> None:
        """Adds another row to the bottom of the table

        Args:
            row (*str): The next row of text to be added to the table
        """
        for col_i in range(0, len(row)):
            self._check_and_increase_max_column_length(col_i, len(row[col_i]))

        self._rows[len(self._rows)] = Row(*row)

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
            Exception: If there is no data, throws an exception.

        Returns:
            str: The currenct table
        """
        if len(self._rows) == 0:
            # TODO: Throw a "table has no length" exception
            raise Exception

        table = self._get_title_row()

        if self.has_header_row:
            table += self._get_header(self._rows[0])

        for i in range(1 if self.has_header_row else 0, len(self._rows)):
            table += self._rows[i].get_row_as_string(
                TABLE_CHARACTER_VERTICAL_BAR,
                [column.max_length for column in self._columns.values()],
            )

        return table + self._bottom_border()

    def clear_title(self) -> None:
        """Clears the title, by setting it to None"""
        self._title = None
        self._title_justification = Justification.CENTRE

    def set_title(
        self, title: str, title_justification: Justification = Justification.CENTRE
    ) -> None:
        """Sets the title and the title's justification.

        Args:
            title (str): The new title of the table
            justification (Justification): The justification for the title of the table. If no justification is passed in, defaults to Justification.CENTRE
        """
        self._title = title
        self._title_justification = title_justification

    def set_title_justification(self, title_justification: Justification) -> None:
        """Sets the title's justification

        Args:
            title_justification (Justification): The justification for the title
        """
        self._title_justification = title_justification

from typing import Sequence
from justification import Justification
from cell import Cell


class Row:
    """An abstraction of the row of the table, which holds each of the cells in that row of the table"""

    def __init__(self, *row: str, justification: Justification | None = None) -> None:
        self.cells: dict[int, Cell] = {}

        for i in range(0, len(row)):
            self.cells[i] = Cell(row[i], justification)

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
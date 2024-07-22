from math import ceil, floor
from .justification import Justification, UnknownJustification


class Cell:
    """The basic building block of the table that stores the text and the justification of itself"""

    def __init__(self, text: str, justification: Justification | None = None) -> None:
        self.justification: Justification | None = justification
        self.text = text

    def _print_as_left_justified(self, max_length: int, border_character: str) -> str:
        """Prints out the cell left-justified

        Args:
            max_length (int): The max length of a cell in this column
            border_character (str): The character to be used on the border at the sides

        Returns:
            str: The cell as a string with left justification
        """
        return (
            " "
            + self.text
            + (" " * (max_length - len(self.text) + 1))
            + border_character
        )

    def _print_as_centre_justified(self, max_length: int, border_character: str) -> str:
        """Prints out the cell centre-justified

        Args:
            max_length (int): The max length of a cell in this column
            border_character (str): The character to be used on the border at the sides

        Returns:
            str: The cell as a string with centre justification
        """
        return (
            " " * (floor((max_length - len(self.text)) / 2) + 1)
            + self.text
            + " " * (ceil((max_length - len(self.text)) / 2) + 1)
            + border_character
        )

    def _print_as_right_justified(self, max_length: int, border_character: str) -> str:
        """Prints out the cell right-justified

        Args:
            max_length (int): The max length of a cell in this column
            border_character (str): The character to be used on the border at the sides

        Returns:
            str: The cell as a string with right justification
        """
        return (
            " " * (max_length - len(self.text) + 1) + self.text + " " + border_character
        )

    def get_cell_as_string(self, max_length: int, border_character: str) -> str:
        """Returns the cell in string format with the correct formatting.
        Note that a justification of None will default to a left justification.

        Args:
            max_length (int): The max length of a cell in that column.
            border_character (str): The character to be used on the border at the sides

        Raises:
            Exception: If there is an incorrect/unsupported justification

        Returns:
            str: The cell as a string with the correct justicication
        """
        # Edge case if there is nothing for this column
        if max_length == 0:
            return " " + border_character

        match self.justification:
            case None:  # Default to left-justified
                return self._print_as_left_justified(max_length, border_character)

            case Justification.LEFT:
                return self._print_as_left_justified(max_length, border_character)

            case Justification.CENTRE:
                return self._print_as_centre_justified(max_length, border_character)

            case Justification.RIGHT:
                return self._print_as_right_justified(max_length, border_character)

            case _:
                raise UnknownJustification

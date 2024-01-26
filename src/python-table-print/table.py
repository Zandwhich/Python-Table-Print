BASE_BORDER = "*"


class PrintTable:
    def __init__(self) -> None:
        self.has_header_row = True

        self._max_column_lengths = []
        self._text = []

    def add_row(self, *row: str) -> None:
        for col_i in range(0, len(row)):
            if (
                len(row[col_i]) > self._max_column_lengths[col_i]
                if col_i < len(self._max_column_lengths)
                else -1
            ):
                if col_i < len(self._max_column_lengths):
                    self._max_column_lengths[col_i] = len(row[col_i])
                else:
                    self._max_column_lengths += [len(row[col_i])]

        self._text += [row]

    def _total_border_length(self) -> int:
        total_border_length = 0

        for col_len in self._max_column_lengths:
            total_border_length += col_len + 3 if not col_len == 0 else 2

        return total_border_length + 1

    def _print_border_row(self) -> None:
        print(BASE_BORDER * self._total_border_length())

    def _print_header(self, header: tuple[str, ...]) -> None:
        self._print_border_row()
        self._print_row(header)
        self._print_border_row()

    def _print_row(self, row: tuple[str, ...]) -> None:
        print(BASE_BORDER, end="")
        for col_i in range(0, len(row)):
            if self._max_column_lengths[col_i] == 0:
                print(" " + BASE_BORDER, end="")
                continue

            print(
                " " * (self._max_column_lengths[col_i] - len(row[col_i]) + 1)
                + row[col_i]
                + " "
                + BASE_BORDER,
                end="",
            )

        print()

    def print_table(self) -> None:
        if len(self._text) == 0:
            # TODO: Throw an error here
            print("ERROR: No text passed in for the table")
            return

        if self.has_header_row:
            self._print_header(self._text[0])

        for r_row in range(1 if self.has_header_row else 0, len(self._text)):
            self._print_row(self._text[r_row])

        self._print_border_row()

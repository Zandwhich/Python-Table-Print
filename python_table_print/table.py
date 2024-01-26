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

    def _get_border_row(self) -> str:
        return BASE_BORDER * self._total_border_length() + "\n"

    def _get_header(self, header: tuple[str, ...]) -> str:
        header = self._get_row(header) + "\n"
        return header + self._get_border_row()

    def _get_row(self, columns: tuple[str, ...]) -> str:
        row = BASE_BORDER
        for col_i in range(0, len(columns)):
            if self._max_column_lengths[col_i] == 0:
                row += " " + BASE_BORDER
                continue

            row += (
                " " * (self._max_column_lengths[col_i] - len(columns[col_i]) + 1)
                + columns[col_i]
                + " "
                + BASE_BORDER
            )

        return row + "\n"

    def get_table(self) -> str:
        if len(self._text) == 0:
            # TODO: Throw an error here
            return "ERROR: No text passed in for the table"

        table = self._get_border_row()

        if self.has_header_row:
            table += self._get_header(self._text[0])

        for r_row in range(1 if self.has_header_row else 0, len(self._text)):
            table += self._get_row(self._text[r_row])

        return table + self._get_border_row()

    def print_table(self) -> None:
        print(self.get_table())

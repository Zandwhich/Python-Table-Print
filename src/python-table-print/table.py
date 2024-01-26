BASE_BORDER = '*'


def print_header(*row: str) -> None:
    max_column_lengths = []

    for col_i in range(0, len(row)):
        if (
            len(row[col_i]) > max_column_lengths[col_i]
            if col_i < len(max_column_lengths)
            else -1
        ):
            if col_i < len(max_column_lengths):
                max_column_lengths[col_i] = len(row[col_i])
            else:
                max_column_lengths += [len(row[col_i])]

    total_border_length = 0

    for col_i in max_column_lengths:
        total_border_length += col_i + 3

    total_border_length += 1

    print(BASE_BORDER * total_border_length)

    print(BASE_BORDER, end='')
    for col_i in row:
        if len(col_i) > 0:
            print(' ' + col_i + ' ' + BASE_BORDER, end='')
        else:
            print(' ' + BASE_BORDER, end='')
    print()

    print(BASE_BORDER * total_border_length)

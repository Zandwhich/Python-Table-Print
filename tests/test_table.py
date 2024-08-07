import sys
import os

import pytest

# Add the parent directory (project root) to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from src.python_table_print import PrintTable, Justification

# Basic Functionality Tests


def test_basic_table():
    table = PrintTable()

    table.add_row("Col 1", "Col 2", "Col 3")
    table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
    table.add_row("Another entry", "yay", "an entry in the table")
    table.add_row("Fun times", "This is kinda cool", "wooow")

    assert (
        table.get_table()
        == """┌───────────────┬────────────────────┬───────────────────────┐
│ Col 1         │ Col 2              │ Col 3                 │
├───────────────┼────────────────────┼───────────────────────┤
│ Entry 1       │ Entry number 2     │ Entry 3 baby          │
│ Another entry │ yay                │ an entry in the table │
│ Fun times     │ This is kinda cool │ wooow                 │
└───────────────┴────────────────────┴───────────────────────┘
"""
    )


def test_extra_columns():
    table = PrintTable()

    table.add_row("Col 1", "Col 2", "Col 3", "Col 4", "Col 5")
    table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
    table.add_row("Another entry", "yay", "an entry in the table")
    table.add_row("Fun times", "This is kinda cool", "wooow")

    assert (
        table.get_table()
        == """┌───────────────┬────────────────────┬───────────────────────┬───────┬───────┐
│ Col 1         │ Col 2              │ Col 3                 │ Col 4 │ Col 5 │
├───────────────┼────────────────────┼───────────────────────┼───────┼───────┤
│ Entry 1       │ Entry number 2     │ Entry 3 baby          │       │       │
│ Another entry │ yay                │ an entry in the table │       │       │
│ Fun times     │ This is kinda cool │ wooow                 │       │       │
└───────────────┴────────────────────┴───────────────────────┴───────┴───────┘
"""
    )


def test_basic_no_header():
    table = PrintTable()

    table.add_row("Col 1", "Col 2", "Col 3")
    table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
    table.add_row("Another entry", "yay", "an entry in the table")
    table.add_row("Fun times", "This is kinda cool", "wooow")
    table.has_header_row = False

    assert (
        table.get_table()
        == """┌───────────────┬────────────────────┬───────────────────────┐
│ Col 1         │ Col 2              │ Col 3                 │
│ Entry 1       │ Entry number 2     │ Entry 3 baby          │
│ Another entry │ yay                │ an entry in the table │
│ Fun times     │ This is kinda cool │ wooow                 │
└───────────────┴────────────────────┴───────────────────────┘
"""
    )


# Justification Tests


def test_table_row_right_justification():
    table = PrintTable()

    table.add_row("Col 1", "Col 2", "Col 3")
    table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
    table.add_row("Another entry", "yay", "an entry in the table")
    table.add_row("Fun times", "This is kinda cool", "wooow")

    table.set_table_justification(Justification.RIGHT)

    with pytest.raises(Exception):
        table.set_table_justification("Something wrong")  # type: ignore

    assert (
        table.get_table()
        == """┌───────────────┬────────────────────┬───────────────────────┐
│         Col 1 │              Col 2 │                 Col 3 │
├───────────────┼────────────────────┼───────────────────────┤
│       Entry 1 │     Entry number 2 │          Entry 3 baby │
│ Another entry │                yay │ an entry in the table │
│     Fun times │ This is kinda cool │                 wooow │
└───────────────┴────────────────────┴───────────────────────┘
"""
    )


def test_table_row_left_justification():
    table = PrintTable()

    table.add_row("Col 1", "Col 2", "Col 3")
    table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
    table.add_row("Another entry", "yay", "an entry in the table")
    table.add_row("Fun times", "This is kinda cool", "wooow")

    table.set_table_justification(Justification.LEFT)

    assert (
        table.get_table()
        == """┌───────────────┬────────────────────┬───────────────────────┐
│ Col 1         │ Col 2              │ Col 3                 │
├───────────────┼────────────────────┼───────────────────────┤
│ Entry 1       │ Entry number 2     │ Entry 3 baby          │
│ Another entry │ yay                │ an entry in the table │
│ Fun times     │ This is kinda cool │ wooow                 │
└───────────────┴────────────────────┴───────────────────────┘
"""
    )


def test_table_row_centre_justification():
    table = PrintTable()

    table.add_row("Col 1", "Col 2", "Col 3")
    table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
    table.add_row("Another entry", "yay", "an entry in the table")
    table.add_row("Fun times", "This is kinda cool", "wooow")

    table.set_table_justification(Justification.CENTRE)

    assert (
        table.get_table()
        == """┌───────────────┬────────────────────┬───────────────────────┐
│     Col 1     │       Col 2        │         Col 3         │
├───────────────┼────────────────────┼───────────────────────┤
│    Entry 1    │   Entry number 2   │     Entry 3 baby      │
│ Another entry │        yay         │ an entry in the table │
│   Fun times   │ This is kinda cool │         wooow         │
└───────────────┴────────────────────┴───────────────────────┘
"""
    )


def test_table_different_row_justification():
    table = PrintTable()

    table.add_row("Col 1", "Col 2", "Col 3")
    table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
    table.add_row("Another entry", "yay", "an entry in the table")
    table.add_row("Fun times", "This is kinda cool", "wooow")

    table.set_row_justification(0, Justification.LEFT)
    table.set_row_justification(1, Justification.CENTRE)
    table.set_row_justification(2, Justification.RIGHT)
    table.set_row_justification(3, Justification.RIGHT)
    table.set_row_justification(3, Justification.LEFT)

    assert (
        table.get_table()
        == """┌───────────────┬────────────────────┬───────────────────────┐
│ Col 1         │ Col 2              │ Col 3                 │
├───────────────┼────────────────────┼───────────────────────┤
│    Entry 1    │   Entry number 2   │     Entry 3 baby      │
│ Another entry │                yay │ an entry in the table │
│ Fun times     │ This is kinda cool │ wooow                 │
└───────────────┴────────────────────┴───────────────────────┘
"""
    )


def test_table_different_column_justification():
    table = PrintTable()

    table.add_row("Col 1", "Col 2", "Col 3")
    table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
    table.add_row("Another entry", "yay", "an entry in the table")
    table.add_row("Fun times", "This is kinda cool", "wooow")

    table.set_column_justification(0, Justification.LEFT)
    table.set_column_justification(1, Justification.CENTRE)
    table.set_column_justification(2, Justification.RIGHT)

    assert (
        table.get_table()
        == """┌───────────────┬────────────────────┬───────────────────────┐
│ Col 1         │       Col 2        │                 Col 3 │
├───────────────┼────────────────────┼───────────────────────┤
│ Entry 1       │   Entry number 2   │          Entry 3 baby │
│ Another entry │        yay         │ an entry in the table │
│ Fun times     │ This is kinda cool │                 wooow │
└───────────────┴────────────────────┴───────────────────────┘
"""
    )


def test_table_different_cell_justification():
    table = PrintTable()

    table.add_row("Col 1", "Col 2", "Col 3")
    table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
    table.add_row("Another entry", "yay", "an entry in the table")
    table.add_row("Fun times", "This is kinda cool", "wooow")

    table.set_row_justification(0, Justification.LEFT)
    table.set_row_justification(1, Justification.CENTRE)
    table.set_cell_justification(1, 2, Justification.RIGHT)
    table.set_row_justification(2, Justification.RIGHT)
    table.set_cell_justification(2, 1, Justification.LEFT)
    table.set_row_justification(3, Justification.RIGHT)
    table.set_row_justification(3, Justification.LEFT)
    table.set_cell_justification(3, 2, Justification.CENTRE)

    assert (
        table.get_table()
        == """┌───────────────┬────────────────────┬───────────────────────┐
│ Col 1         │ Col 2              │ Col 3                 │
├───────────────┼────────────────────┼───────────────────────┤
│    Entry 1    │   Entry number 2   │          Entry 3 baby │
│ Another entry │ yay                │ an entry in the table │
│ Fun times     │ This is kinda cool │         wooow         │
└───────────────┴────────────────────┴───────────────────────┘
"""
    )


def test_table_with_title_centred():
    table = PrintTable()

    table.add_row("Col 1", "Col 2", "Col 3")
    table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
    table.add_row("Another entry", "yay", "an entry in the table")
    table.add_row("Fun times", "This is kinda cool", "wooow")

    table.set_title("Title")

    assert (
        table.get_table()
        == """┌────────────────────────────────────────────────────────────┐
│                           Title                            │
├───────────────┬────────────────────┬───────────────────────┤
│ Col 1         │ Col 2              │ Col 3                 │
├───────────────┼────────────────────┼───────────────────────┤
│ Entry 1       │ Entry number 2     │ Entry 3 baby          │
│ Another entry │ yay                │ an entry in the table │
│ Fun times     │ This is kinda cool │ wooow                 │
└───────────────┴────────────────────┴───────────────────────┘
"""
    )


def test_table_with_title_left_justified():
    table = PrintTable()

    table.add_row("Col 1", "Col 2", "Col 3")
    table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
    table.add_row("Another entry", "yay", "an entry in the table")
    table.add_row("Fun times", "This is kinda cool", "wooow")

    table.set_title("Title", Justification.LEFT)

    assert (
        table.get_table()
        == """┌────────────────────────────────────────────────────────────┐
│ Title                                                      │
├───────────────┬────────────────────┬───────────────────────┤
│ Col 1         │ Col 2              │ Col 3                 │
├───────────────┼────────────────────┼───────────────────────┤
│ Entry 1       │ Entry number 2     │ Entry 3 baby          │
│ Another entry │ yay                │ an entry in the table │
│ Fun times     │ This is kinda cool │ wooow                 │
└───────────────┴────────────────────┴───────────────────────┘
"""
    )


def test_table_with_title_right_justified():
    table = PrintTable()

    table.add_row("Col 1", "Col 2", "Col 3")
    table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
    table.add_row("Another entry", "yay", "an entry in the table")
    table.add_row("Fun times", "This is kinda cool", "wooow")

    table.set_title("Title")
    table.set_title_justification(Justification.RIGHT)

    assert (
        table.get_table()
        == """┌────────────────────────────────────────────────────────────┐
│                                                      Title │
├───────────────┬────────────────────┬───────────────────────┤
│ Col 1         │ Col 2              │ Col 3                 │
├───────────────┼────────────────────┼───────────────────────┤
│ Entry 1       │ Entry number 2     │ Entry 3 baby          │
│ Another entry │ yay                │ an entry in the table │
│ Fun times     │ This is kinda cool │ wooow                 │
└───────────────┴────────────────────┴───────────────────────┘
"""
    )


def test_table_with_a_very_long_title():
    table = PrintTable()

    table.add_row("Col 1", "Col 2", "Col 3")
    table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
    table.add_row("Another entry", "yay", "an entry in the table")
    table.add_row("Fun times", "This is kinda cool", "wooow")

    table.set_title(
        "This is a title that is way, way, way, way, way, way too long and will certainly be truncated"
    )

    assert (
        table.get_table()
        == """┌────────────────────────────────────────────────────────────┐
│ This is a title that is way, way, way, way, way, way too l │
├───────────────┬────────────────────┬───────────────────────┤
│ Col 1         │ Col 2              │ Col 3                 │
├───────────────┼────────────────────┼───────────────────────┤
│ Entry 1       │ Entry number 2     │ Entry 3 baby          │
│ Another entry │ yay                │ an entry in the table │
│ Fun times     │ This is kinda cool │ wooow                 │
└───────────────┴────────────────────┴───────────────────────┘
"""
    )


def test_table_with_a_cleared_title():
    table = PrintTable()

    table.add_row("Col 1", "Col 2", "Col 3")
    table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
    table.add_row("Another entry", "yay", "an entry in the table")
    table.add_row("Fun times", "This is kinda cool", "wooow")

    table.set_title("Title")
    table.clear_title()

    assert (
        table.get_table()
        == """┌───────────────┬────────────────────┬───────────────────────┐
│ Col 1         │ Col 2              │ Col 3                 │
├───────────────┼────────────────────┼───────────────────────┤
│ Entry 1       │ Entry number 2     │ Entry 3 baby          │
│ Another entry │ yay                │ an entry in the table │
│ Fun times     │ This is kinda cool │ wooow                 │
└───────────────┴────────────────────┴───────────────────────┘
"""
    )


def test_incorrect_title_justificion():
    table = PrintTable()

    table.add_row("this", "is", "my", "row")
    table.set_title("This is my title")

    table._title_justification = "Overwriting the title justification with an erroneous value"  # type: ignore

    with pytest.raises(Exception):
        table.get_table()


# Other tests/errors


def test_incorrect_cell_justifcation():
    table = PrintTable()

    table.add_row("a single entry")
    table._rows[0].cells[0].justification = "This is a wrong justification"  # type: ignore

    with pytest.raises(Exception):
        table.get_table()


def test_empty_rows_and_columns():
    table = PrintTable()

    table.add_row("Not Empty", "", "", "", "")
    table.add_row("", "", "", "", "")
    table.add_row("", "", "", "", "")

    table.set_title("Title")

    assert (
        table.get_table()
        == """┌───────────────────┐
│       Title       │
├───────────┬─┬─┬─┬─┤
│ Not Empty │ │ │ │ │
├───────────┼─┼─┼─┼─┤
│           │ │ │ │ │
│           │ │ │ │ │
└───────────┴─┴─┴─┴─┘
"""
    )


def test_no_table():
    table = PrintTable()

    with pytest.raises(Exception):
        table.get_table()

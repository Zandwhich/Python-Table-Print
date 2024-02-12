import sys
import os

# Add the parent directory (project root) to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from src.python_table_print import PrintTable


def test_basic_table():
    table = PrintTable()

    table.add_row("Col 1", "Col 2", "Col 3")
    table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
    table.add_row("Another entry", "yay", "an entry in the table")
    table.add_row("Fun times", "This is kinda cool", "wooow")

    assert (
        table.get_table()
        == """**************************************************************
*         Col 1 *              Col 2 *                 Col 3 *
**************************************************************
*       Entry 1 *     Entry number 2 *          Entry 3 baby *
* Another entry *                yay * an entry in the table *
*     Fun times * This is kinda cool *                 wooow *
**************************************************************
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
        == """**************************************************************
*         Col 1 *              Col 2 *                 Col 3 *
*       Entry 1 *     Entry number 2 *          Entry 3 baby *
* Another entry *                yay * an entry in the table *
*     Fun times * This is kinda cool *                 wooow *
**************************************************************
"""
    )


def test_extra_columns():
    table = PrintTable()
    
    table.add_row("Col 1", "Col 2", "Col 3", "Col 4", "Col 5")
    table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
    table.add_row("Another entry", "yay", "an entry in the table")
    table.add_row("Fun times", "This is kinda cool", "wooow")
    table.has_header_row = True

    assert (
        table.get_table()
        == """******************************************************************************
*         Col 1 *              Col 2 *                 Col 3 * Col 4 * Col 5 *
******************************************************************************
*       Entry 1 *     Entry number 2 *          Entry 3 baby *       *       *
* Another entry *                yay * an entry in the table *       *       *
*     Fun times * This is kinda cool *                 wooow *       *       *
******************************************************************************
"""
    )

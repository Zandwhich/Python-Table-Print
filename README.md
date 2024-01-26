# Python Table Print
A project to dynamically scale and print tables using text in Python

# Usage

Python Table Print is object-oriented. This means that a `PrintTable` object gets instantiated and added to/edited. When the table is ready to be printed/created, this can be done by calling the `print_table`/`get_table` methods. An example can be found in `example.py`, but is copied here for convenience:

```python
from table import PrintTable

my_table = PrintTable()

my_table.add_row("Col 1", "Col 2", "Col 3")
my_table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
my_table.add_row("Another entry", "yay", "an entry in the table")
my_table.add_row("Fun times", "This is kinda cool", "wooow")

my_table.print_table()
```

Output:
```
**************************************************************
*         Col 1 *              Col 2 *                 Col 3 *
**************************************************************
*       Entry 1 *     Entry number 2 *          Entry 3 baby *
* Another entry *                yay * an entry in the table *
*     Fun times * This is kinda cool *                 wooow *
**************************************************************
```

In the above example, the `print_table` method was called which prints using the default `print` function. However, if the table in string form is preferred, then this is also easily achievable:

```python
from table import PrintTable

my_table = PrintTable()

...

str_table = my_table.get_table()
```

## Header

By default, the first row of the table is treated as the header of the table, and is printed with an extra border around it, not done for any other row. This behaviour can be turned off/on by setting the property `has_header` to `True`/`False`:

```python
from table import PrintTable

table = PrintTable()

table.add_row("Col 1", "Col 2", "Col 3")
table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
table.add_row("Another entry", "yay", "an entry in the table")
table.add_row("Fun times", "This is kinda cool", "wooow")
table.has_header_row = False

table.print_table()
```

Output:
```
**************************************************************
*         Col 1 *              Col 2 *                 Col 3 *
*       Entry 1 *     Entry number 2 *          Entry 3 baby *
* Another entry *                yay * an entry in the table *
*     Fun times * This is kinda cool *                 wooow *
**************************************************************
```
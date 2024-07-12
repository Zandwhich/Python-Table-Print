[![PyPi Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FZandwhich%2FPython-Table-Print%2Fmaster%2Fpyproject.toml&query=project.version&label=version&color=bright%20green
)](https://pypi.org/project/python-table-print/) [![codecov](https://img.shields.io/codecov/c/github/Zandwhich/Python-Table-Print
)]()

# Python Table Print
A lightweight library to create ASCII tables that automaticallly update their spacing based on the input.

# Usage

Python Table Print is object-oriented. This means that a `PrintTable` object gets instantiated and added to/edited. When the table is ready to be printed/created, this can be done by calling the `get_table` method. An example can be found in `example.py`, but is copied here for convenience:

## Basic Usage

```python
from table import PrintTable

my_table = PrintTable()

my_table.add_row("Col 1", "Col 2", "Col 3")
my_table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
my_table.add_row("Another entry", "yay", "an entry in the table")
my_table.add_row("Fun times", "This is kinda cool", "wooow")

print(my_table.get_table())
```

Output:
```
┌───────────────┬────────────────────┬───────────────────────┐
│ Col 1         │ Col 2              │ Col 3                 │
├───────────────┼────────────────────┼───────────────────────┤
│ Entry 1       │ Entry number 2     │ Entry 3 baby          │
│ Another entry │ yay                │ an entry in the table │
│ Fun times     │ This is kinda cool │ wooow                 │
└───────────────┴────────────────────┴───────────────────────┘
```

As shown in the above example, getting the current table is as simple as calling the `get_table()` method. This returns the table as a simple string. This can then be passed to whatever function you like, in this case the `print` function.

## Header

By default, the first row of the table is treated as the header of the table, and is printed with an extra border around it, not done for any other row. This behaviour can be turned off/on by setting the property `has_header` to `True`/`False`:

```python
from table import PrintTable

my_table = PrintTable()

my_table.add_row("Col 1", "Col 2", "Col 3")
my_table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
my_table.add_row("Another entry", "yay", "an entry in the table")
my_table.add_row("Fun times", "This is kinda cool", "wooow")

my_table.has_header_row = False

print(my_table.get_table())
```

Output:
```
┌───────────────┬────────────────────┬───────────────────────┐
│ Col 1         │ Col 2              │ Col 3                 │
│ Entry 1       │ Entry number 2     │ Entry 3 baby          │
│ Another entry │ yay                │ an entry in the table │
│ Fun times     │ This is kinda cool │ wooow                 │
└───────────────┴────────────────────┴───────────────────────┘
```

## Justification

Be default, all of the cells are justified to the left. However, justification can be changed for the entire table, for a row or column, or for individual cells. Whenever a justification is set it overrides any previous justification set on that/those cell/cells. Note that `Justification` also needs to be imported.

### Justification for the Table:

```python
from table import PrintTable, Justification

my_table = PrintTable()

my_table.add_row("Col 1", "Col 2", "Col 3")
my_table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
my_table.add_row("Another entry", "yay", "an entry in the table")
my_table.add_row("Fun times", "This is kinda cool", "wooow")

my_table.set_table_justification(Justification.CENTRE)

print(my_table.get_table())
```

Output:
```
┌───────────────┬────────────────────┬───────────────────────┐
│     Col 1     │       Col 2        │         Col 3         │
├───────────────┼────────────────────┼───────────────────────┤
│    Entry 1    │   Entry number 2   │     Entry 3 baby      │
│ Another entry │        yay         │ an entry in the table │
│   Fun times   │ This is kinda cool │         wooow         │
└───────────────┴────────────────────┴───────────────────────┘
```

### Justification for a Row:

Continuing from the previous example above:
```python
...

my_table.set_row_justification(0, Justification.LEFT)

print(my_table.get_table())
```

Output:
```
┌───────────────┬────────────────────┬───────────────────────┐
│ Col 1         │ Col 2              │ Col 3                 │
├───────────────┼────────────────────┼───────────────────────┤
│    Entry 1    │   Entry number 2   │     Entry 3 baby      │
│ Another entry │        yay         │ an entry in the table │
│   Fun times   │ This is kinda cool │         wooow         │
└───────────────┴────────────────────┴───────────────────────┘
```

### Justification for a Column:

Continuing from the previous example above:
```python
...

my_table.set_column_justification(0, Justification.RIGHT)

print(my_table.get_table())
```

Output:
```
┌───────────────┬────────────────────┬───────────────────────┐
│         Col 1 │ Col 2              │ Col 3                 │
├───────────────┼────────────────────┼───────────────────────┤
│       Entry 1 │   Entry number 2   │     Entry 3 baby      │
│ Another entry │        yay         │ an entry in the table │
│     Fun times │ This is kinda cool │         wooow         │
└───────────────┴────────────────────┴───────────────────────┘
```

### Justification for a Cell:

Continuing from the previous example above:
```python
...

my_table.set_cell_justification(1, 1, Justification.LEFT)

print(my_table.get_table())
```

Output:
```
┌───────────────┬────────────────────┬───────────────────────┐
│         Col 1 │ Col 2              │ Col 3                 │
├───────────────┼────────────────────┼───────────────────────┤
│       Entry 1 │ Entry number 2     │     Entry 3 baby      │
│ Another entry │        yay         │ an entry in the table │
│     Fun times │ This is kinda cool │         wooow         │
└───────────────┴────────────────────┴───────────────────────┘
```

Notice how in the above examples the justifications of the edited cells were overwritten with the latest justification.

## Title

You can add a title to your table. Defaults to centre justification

```python
...

my_table.set_title("Title")
```

Output:
```
┌────────────────────────────────────────────────────────────┐
│                           Title                            │
├───────────────┬────────────────────┬───────────────────────┤
│         Col 1 │ Col 2              │ Col 3                 │
├───────────────┼────────────────────┼───────────────────────┤
│       Entry 1 │ Entry number 2     │     Entry 3 baby      │
│ Another entry │        yay         │ an entry in the table │
│     Fun times │ This is kinda cool │         wooow         │
└───────────────┴────────────────────┴───────────────────────┘
```

Clearing a title:

```python
...

my_table.clear_title()
```

Output:
```
┌───────────────┬────────────────────┬───────────────────────┐
│         Col 1 │ Col 2              │ Col 3                 │
├───────────────┼────────────────────┼───────────────────────┤
│       Entry 1 │ Entry number 2     │     Entry 3 baby      │
│ Another entry │        yay         │ an entry in the table │
│     Fun times │ This is kinda cool │         wooow         │
└───────────────┴────────────────────┴───────────────────────┘
```

### Justification for Title

You can change the justification of your title:

```python
...

my_table.set_title("Title")
my_table.set_title_justification(Justification.LEFT)
```

Output:
```
┌────────────────────────────────────────────────────────────┐
│ Title                                                      │
├───────────────┬────────────────────┬───────────────────────┤
│         Col 1 │ Col 2              │ Col 3                 │
├───────────────┼────────────────────┼───────────────────────┤
│       Entry 1 │ Entry number 2     │     Entry 3 baby      │
│ Another entry │        yay         │ an entry in the table │
│     Fun times │ This is kinda cool │         wooow         │
└───────────────┴────────────────────┴───────────────────────┘
```
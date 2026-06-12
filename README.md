[![PyPi Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FZandwhich%2FPython-Table-Print%2Fmaster%2Fpyproject.toml&query=project.version&label=version&color=bright%20green&logo=pypi)](https://pypi.org/project/python-table-print/) [![python version](https://img.shields.io/pypi/pyversions/python-table-print?logo=python)](https://pypi.org/project/python-table-print/) [![downloads](https://img.shields.io/pypi/dm/python-table-print?logo=pypi)](https://pypi.org/project/python-table-print/) [![codecov](https://img.shields.io/codecov/c/github/Zandwhich/Python-Table-Print?logo=codecov)](https://app.codecov.io/github/Zandwhich/Python-Table-Print)

# Python Table Print

A lightweight Python library for generating ASCII tables that automatically adjust their column widths to fit your data.

## Installation

```
pip install python-table-print
```

## Quick Start

`PrintTable` is the core class — add rows to it, then call `get_table()` to retrieve the formatted table as a string:

```python
from table import PrintTable, Justification

schedule = PrintTable()
schedule.set_title("Solar System at a Glance")

schedule.add_row("Planet", "Type", "Moons", "Day Length", "Claim to Fame")
schedule.add_row("Mercury", "Terrestrial", "0",   "59 days",    "Closest to the Sun")
schedule.add_row("Venus",   "Terrestrial", "0",   "243 days",   "Hottest surface")
schedule.add_row("Earth",   "Terrestrial", "1",   "24 hours",   "Only known life")
schedule.add_row("Mars",    "Terrestrial", "2",   "24.6 hours", "Home of Olympus Mons")
schedule.add_row("Jupiter", "Gas giant",   "95",  "9.9 hours",  "Largest planet")
schedule.add_row("Saturn",  "Gas giant",   "146", "10.7 hours", "The ringed beauty")
schedule.add_row("Uranus",  "Ice giant",   "28",  "17.2 hours", "Rotates on its side")
schedule.add_row("Neptune", "Ice giant",   "16",  "16.1 hours", "Farthest from Sun")

schedule.set_column_justification(2, Justification.RIGHT)

print(schedule.get_table())
```

```
┌───────────────────────────────────────────────────────────────────┐
│                      Solar System at a Glance                     │
├─────────┬─────────────┬───────┬────────────┬──────────────────────┤
│ Planet  │ Type        │ Moons │ Day Length │ Claim to Fame        │
├─────────┼─────────────┼───────┼────────────┼──────────────────────┤
│ Mercury │ Terrestrial │     0 │ 59 days    │ Closest to the Sun   │
│ Venus   │ Terrestrial │     0 │ 243 days   │ Hottest surface      │
│ Earth   │ Terrestrial │     1 │ 24 hours   │ Only known life      │
│ Mars    │ Terrestrial │     2 │ 24.6 hours │ Home of Olympus Mons │
│ Jupiter │ Gas giant   │    95 │ 9.9 hours  │ Largest planet       │
│ Saturn  │ Gas giant   │   146 │ 10.7 hours │ The ringed beauty    │
│ Uranus  │ Ice giant   │    28 │ 17.2 hours │ Rotates on its side  │
│ Neptune │ Ice giant   │    16 │ 16.1 hours │ Farthest from Sun    │
└─────────┴─────────────┴───────┴────────────┴──────────────────────┘
```

`get_table()` returns the table as a plain string, so it can be passed to any function — not just `print`.

## Usage

### Header Row

By default, the first row is treated as a header and rendered with a separator below it. This can be toggled via the `has_header_row` property:

```python
my_table.has_header_row = False
```

### Title

A title can be added above the table with `set_title()`. It defaults to centre justification:

```python
my_table.set_title("My Title")
```

To remove the title, call `clear_title()`.

### Justification

By default, all cells are left-justified. Justification can be set at four levels of granularity — each level overrides any previously set justification for the affected cells. The `Justification` enum must be imported alongside `PrintTable`.

#### Table-wide

```python
from table import PrintTable, Justification

my_table.set_table_justification(Justification.CENTRE)
```

#### Row

```python
my_table.set_row_justification(0, Justification.LEFT)
```

#### Column

```python
my_table.set_column_justification(0, Justification.RIGHT)
```

#### Cell

```python
my_table.set_cell_justification(1, 1, Justification.LEFT)
```

Justification for the title can also be set independently:

```python
my_table.set_title_justification(Justification.LEFT)
```

## License

[MIT](LICENSE)

This was made as a way to learn how to publish projects to PyPi. No AI was used in the making of this project, except
for this README.

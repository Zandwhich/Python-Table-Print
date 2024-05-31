from table import PrintTable, Justification

# Create a basic table

my_table = PrintTable()

my_table.add_row("Col 1", "Col 2", "Col 3")
my_table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
my_table.add_row("Another entry", "yay", "an entry in the table")
my_table.add_row("Fun times", "This is kinda cool", "wooow")

print("Basic Table\n")
print(my_table.get_table())
print("\n\n")


# The header row is optional and can be removed

my_table.has_header_row = False

print("Table Without Header\n")
print(my_table.get_table())
print("\n\n")


# You can set the justification for the whole table, for a row or column, or for an individual cell.
# Each justification command overrides any previous justification set for those cell(s)

my_table.has_header_row = True

my_table.set_table_justification(Justification.CENTRE)

print("Table With Centre Justification\n")
print(my_table.get_table())
print("\n\n")

my_table.set_row_justification(0, Justification.LEFT)

print("Table With Top Row Left-Justified\n")
print(my_table.get_table())
print("\n\n")

my_table.set_column_justification(0, Justification.RIGHT)

print("Table With First Column Right-Justified\n")
print(my_table.get_table())
print("\n\n")

my_table.set_cell_justification(1, 1, Justification.LEFT)

print("Table With One Cell Left-Justified\n")
print(my_table.get_table())
print("\n\n")

my_table.set_title("Title")

print("Table With Title With Centre Justification\n")
print(my_table.get_table())
print("\n\n")

my_table.set_title_justification(Justification.LEFT)

print("Table With Title With Left Justification\n")
print(my_table.get_table())
print("\n\n")

my_table.set_title_justification(Justification.RIGHT)

print("Table With Title With Right Justification\n")
print(my_table.get_table())
print("\n\n")

my_table.clear_title()

print("Table With Cleared Title\n")
print(my_table.get_table())
print("\n\n")

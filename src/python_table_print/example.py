from table import PrintTable, Justification

# Create a basic table

table = PrintTable()

table.add_row("Col 1", "Col 2", "Col 3")
table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
table.add_row("Another entry", "yay", "an entry in the table")
table.add_row("Fun times", "This is kinda cool", "wooow")

print("Basic Table\n")
print(table.get_table())
print("\n\n")


# The header row is optional and can be removed

table.has_header_row = False

print("Table Without Header\n")
print(table.get_table())
print("\n\n")


# You can set the justification for the whole table, for a row or column, or for an individual cell. Each justification command overrides any previous justification set for those cell(s)

table.has_header_row = True

table.set_table_justification(Justification.CENTRE)

print("Table With Centre Justification\n")
print(table.get_table())
print("\n\n")

table.set_row_justification(0, Justification.LEFT)

print("Table With Top Row Left-Justified\n")
print(table.get_table())
print("\n\n")

table.set_column_justification(0, Justification.RIGHT)

print("Table With First Column Right-Justified\n")
print(table.get_table())
print("\n\n")

table.set_cell_justification(1, 1, Justification.LEFT)

print("Table With One Cell Left-Justified\n")
print(table.get_table())
print("\n\n")

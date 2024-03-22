from table import PrintTable, Justification

table = PrintTable()

table.add_row("Col 1", "Col 2", "Col 3")
table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
table.add_row("Another entry", "yay", "an entry in the table")
table.add_row("Fun times", "This is kinda cool", "wooow")

table.has_header_row = True

table.set_row_justification(0, Justification.LEFT)
table.set_row_justification(1, Justification.CENTRE)
table.set_cell_justification(1, 2, Justification.RIGHT)
table.set_row_justification(2, Justification.RIGHT)
table.set_cell_justification(2, 1, Justification.LEFT)
table.set_row_justification(3, Justification.RIGHT)
table.set_row_justification(3, Justification.LEFT)
table.set_cell_justification(3, 2, Justification.CENTRE)

table.set_column_justification(2, Justification.RIGHT)

print(table.get_table())

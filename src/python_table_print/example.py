from table import PrintTable

table = PrintTable()

table.add_row("Col 1", "Col 2", "Col 3")
table.add_row("Entry 1", "Entry number 2", "Entry 3 baby")
table.add_row("Another entry", "yay", "an entry in the table")
table.add_row("Fun times", "This is kinda cool", "wooow")
table.has_header_row = False

table.print_table()

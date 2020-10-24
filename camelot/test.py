import camelot
tables = camelot.read_pdf("5.pdf", pages="2,3,4,5,6")
print(tables)
tables.export('foo.csv', f='csv', compress=True)
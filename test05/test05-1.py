from openpyxl import load_workbook
wb = load_workbook(filename='sample.xlsx', read_only=True)
ws = wb['Testdata']

for row in ws.rows:
    for cell in row:
        print(cell.value)
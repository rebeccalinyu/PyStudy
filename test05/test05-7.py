from openpyxl import Workbook

wb = Workbook()
dest_filename = 'sample-2.xlsx'

ws = wb.active
ws.title = "test-1"

ws["A2"] = "=SUM(2, 1)"
wb.save(filename = dest_filename)

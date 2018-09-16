from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import nester_06

dest_filename = 'sample-2.xlsx'
wb = load_workbook(dest_filename)

ws = wb['test-2']

nester_06.mergecell(ws)

wb.save(filename = dest_filename)
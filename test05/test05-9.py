from openpyxl.workbook import Workbook
from openpyxl.drawing.image import Image
import nester_07

wb = Workbook()
dest_filename = 'sample-2.xlsx'

ws = wb.active
ws.title = "test-1"

nester_07.insertimage(ws)

wb.save(filename = dest_filename)
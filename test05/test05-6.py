import datetime
from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter

wb = Workbook()
dest_filename = 'sample-2.xlsx'

ws1 = wb.active
ws1.title = "test-1"
ws1['A1'] = datetime.datetime(2010, 7, 20)
ws1['A1'].number_format
'yyyy-mm-dd h:mm:ss'
# You can enable type inference on a case-by-case basis
wb.guess_types = True
# set percentage using a string followed by the percent sign

ws1['B1'] = '3.14%'
wb.guess_types = False
ws1['B1'].value
ws1['B1'].number_format

wb.save(filename = dest_filename)

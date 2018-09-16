from openpyxl import load_workbook
wb = load_workbook(filename = 'samplenew.xlsx')
sheet_ranges = wb['OS Exp']
print(sheet_ranges['C3'].value)
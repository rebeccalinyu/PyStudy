from openpyxl import Workbook
from openpyxl.drawing.image import Image

def insertimage(ws):
   
# create an image
    img = Image('torry.jpg')
    ws.add_image(img, 'A1')
    print(ws.title)
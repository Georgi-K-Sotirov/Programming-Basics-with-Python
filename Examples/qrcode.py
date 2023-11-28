import pyqrcode
import png
from pyqrcode import QRCode

address = 'Georgi Sotirov +359878265667'
url = pyqrcode.create(address)
url.png('Georgi Sotirov.png', scale = 8)
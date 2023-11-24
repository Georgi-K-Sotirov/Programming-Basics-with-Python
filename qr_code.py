import pyqrcode
import png
from pyqrcode import QRCode

address = 'https://sportal.bg/'
url = pyqrcode.create(address)
url.png('sportal.png', scale=8)

from pyzbar.pyzbar import decode
from PIL import Image
import os

path = os.path.expanduser('~/Pictures/Pytohn/Qr.png')

img = Image.open(path)

result = decode(img)
print(result)
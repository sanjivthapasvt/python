import qrcode
import os

data = input("Enter the data you want to encode: ")
img = qrcode.make(data)

path = os.path.expanduser('~/Pictures/Pytohn/Qr.png')
os.makedirs(os.path.dirname(path), exist_ok=True)

try:
    img.save(path)
    print(f"QR sucessfully saved to {path}")
except Exception as e:
    print("Some error has occured")
import pyqrcode

link = input("Enter link to generate QR code :- ")
url = pyqrcode.create(link)
url.svg("QRCode.svg", scale=8)
print("="*40)
print("QR code generated")
print("="*40)

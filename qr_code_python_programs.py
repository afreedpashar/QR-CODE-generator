import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_H,
              box_size=8,border=4)
qr.add_data("https://github.com/afreedpashar/Python-Progams")
qr.make(fit=True)
img = qr.make_image(fill_color="black",back_color="white")
img.save("python-programs.png")

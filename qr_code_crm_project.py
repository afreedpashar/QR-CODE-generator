import qrcode 
from PIL import Image

qr = qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_H,
                   box_size=5,border=4)
qr.add_data("https://github.com/afreedpashar/Django_DCRM/tree/master/dcrm")
qr.make(fit=True)
img = qr.make_image(fill_color="blue",back_color="white")
img.save("Django-CRM-project.png")



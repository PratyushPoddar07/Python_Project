import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=8,border=4)

qr.add_data("https://github.com/PratyushPoddar07")
qr.make(fit=True)
img = qr.make_image(fill_color = "purple",back_color="white")
img.save("Github-QRcode.png")
import image
import qrcode

qr = qrcode.QRCode(
    version= 4, # greater version num, more num of b/w dots increases
    box_size=3, #dimension of qrcode image
    border=5 #white corner border of img
)
# Data for which you want to make QR code
data = "http://efrontech.in"

qr.add_data(data)

qr.make(fit=True)

# Generating the QR code
img = qr.make_image(fill="black", back_color ="white")

# File name of the QR code Image and save it
img.save("QR-CODE.png")
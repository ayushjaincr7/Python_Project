# import qrcode

# data = 'Don\'t forget to subscribe'

# # img = qrcode.make(data)

# # img.save('MyQrCode.png')

# qr = qrcode.QRCode(
#     version=1,
#     box_size=10,
#     border=5
# )

# qr.add_data(data)
# qr.make(fit=True)

# img = qr.make_image(fill_color="red", back_color = "white")
# img.save('myqrcode.png')

from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('qrCode/MyQrCode.png')


result = decode(img)

print(result)



# You may need to install 'image' and 'qrcode' modules
import qrcode
import random
import string

TheInput = input('Type the text you want to convert: ')
name = string.ascii_letters + string.digits
fileName = "".join(random.sample(name,10)) + '.png'
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr.add_data(input)
qr.make(fit=True)

img = qr.make_image(fill_color="skyblue", back_color="white")
img.save(fileName)

print(qr.data_list)

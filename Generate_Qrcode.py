# You may need to install 'image' and 'qrcode' modules
import qrcode

input_URL = "hamza hammadi"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr.add_data(input_URL)
qr.make(fit=True)

img = qr.make_image(fill_color="skyblue", back_color="white")
img.save("qrcode.png")

print(qr.data_list)
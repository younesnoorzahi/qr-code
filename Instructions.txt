# Pure python QR Code generator
pip install qrcode

# Usage
# From the command line, use the installed qr script:
qr "Some text" > test.png

#Or in Python, use the make shortcut function:
import qrcode
img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")


# Advanced Usage
# For more control, use the QRCode class. For example:
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

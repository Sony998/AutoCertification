import qrcode

# Data to encode
data = "mailto:medicsionsas@gmail.com"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the instance
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("qrcode_mailto.png")
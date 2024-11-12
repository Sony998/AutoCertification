import qrcode
from PIL import Image, ImageDraw, ImageFont
import json
import pandas as pd
import os

archivo_excel = 'pulido.xlsx'
df = pd.read_excel(archivo_excel, sheet_name='BASCULAS DE PISO', header=None)   
fila_actual = 5

output_directory = "PULIR/Basculas/QRS"
with open("file_urls.json", "r") as file:
    data = json.load(file)
links = [value for key, value in data.items()]
certificados = [key for key, value in data.items()]
qr_images = []

for link in links:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=18,
        border=1,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    qr_images.append(img.convert("RGBA"))

background_template = Image.open("backqr.png")
series = [str(df.iat[fila_actual + i * 19 + 1, 7]) for i in range(min(len(certificados), (len(df) - fila_actual) // 19))]
bg_width, bg_height = background_template.size
constant_text2 = "7 de noviembre de 2024"
font = ImageFont.truetype("Arial.ttf", 80)
font2 = ImageFont.truetype("Arial.ttf", 50)
fila_actual += 19

for i, certificado in enumerate(certificados):
    print(f"Certificado: {certificado}, Serie: {series[i]}")
    background = background_template.copy()
    draw = ImageDraw.Draw(background)
    draw.text((130, 580), certificado, font=font, fill="white")
    draw.text((210, 722), constant_text2, font=font2, fill="white")
    draw.text((200, 815), series[i], font=font2, fill="white")
    qr_width, qr_height = qr_images[i].size
    pos = (int((bg_width / 2) + 200), int((bg_height / 2) - 40))
    background.paste(qr_images[i], pos, qr_images[i])
    background.save(f"{output_directory}/{certificado}.png")

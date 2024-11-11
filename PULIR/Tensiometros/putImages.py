from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image, ImageDraw, ImageFont
import os
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import pandas as pd


archivo_excel = 'pulido.xlsx'   
df = pd.read_excel(archivo_excel, sheet_name='TENSIOMETROS', header=None)
fila_actual = 5
errores_promedio = []
desviaciones = []
certificados = []
while True:
    if fila_actual >= len(df):
        break
    error_promedio = df.iat[fila_actual + 8, 1]
    desviacion = df.iat[fila_actual +9, 1]
    certficado = df.iat[fila_actual, 7]
    certificados.append(certficado)
    desviaciones.append(desviacion)
    errores_promedio.append(error_promedio)
    print(f"Certificado: {certficado}, Error promedio: {error_promedio}, desviacion {desviacion}")
    fila_actual += 19


def agregar_imagenes_pdf(img_fondo_path, img_superior_path1, img_superior_path2, output_pdf_path, yinferior, ysuperior, error_promedio, desviacion):
    img_fondo = Image.open(img_fondo_path).convert("RGBA")
    image_superior = Image.open(img_superior_path1).convert("RGBA")
    image_inferior = Image.open(img_superior_path2).convert("RGBA")
    
    carta_ancho, carta_alto = letter
    fondo_path = "temp_fondo.png"
    img_fondo.save(fondo_path, format="PNG")  
    image_superior = image_superior.resize((int(image_superior.width / 6), int(image_superior.height / 6)), Image.LANCZOS)
    image_inferior = image_inferior.resize((int(image_inferior.width / 6), int(image_inferior.height / 6)), Image.LANCZOS)
    # Calcular la posición de las imágenes
    x_fondo = 0  # Colocar el fondo en 0 para ocupar toda la página
    xsuperior = (carta_ancho - image_inferior.width) // 2 - 30
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    c.drawImage(fondo_path, x_fondo, 0, width=carta_ancho, height=carta_alto, preserveAspectRatio=True, mask='auto')
    c.drawImage(img_superior_path1, xsuperior, yinferior, width=image_superior.width, height=image_superior.height)
    c.drawImage(img_superior_path2, xsuperior, ysuperior, width=image_inferior.width, height=image_inferior.height)
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.TTF'))
    c.setFont("Arial", 15)
    c.drawString(350, 678, "{:.2f}".format(float(f"{error_promedio:.2f}")))
    c.drawString(350, 659, "{:.2f}".format(float(f"{desviacion:.2f}")))
    c.save()

# Rutas de las imágenes y carpetas
img_fondo_path = "PULIR/Tensiometros/partesReporte/Pagina3.png"
output_directory = "PULIR/Tensiometros/Reportes/3"
inferior_directory = "PULIR/Tensiometros/Graficos/Error"
superior_directory = "PULIR/Tensiometros/Graficos/Desviacion"
errorpos = 0
for certficado in certificados:
    img_superior_path1 = os.path.join(inferior_directory, certficado + ".png")
    img_superior_path2 = os.path.join(superior_directory, certficado + ".png")
    output_pdf_path = os.path.join(output_directory, certficado + ".pdf")
    agregar_imagenes_pdf(img_fondo_path, img_superior_path1, img_superior_path2, output_pdf_path, 
                         yinferior=125, ysuperior=378, error_promedio=errores_promedio[errorpos], desviacion=desviaciones[errorpos])
    print(f"Se ha creado el archivo {output_pdf_path}","con error promedio de", errores_promedio[errorpos])
    errorpos += 1

""" for filename in os.listdir(inferior_directory):
    if filename in os.listdir(superior_directory):
        img_superior_path1 = os.path.join(inferior_directory, filename)
        img_superior_path2 = os.path.join(superior_directory, filename)
        output_pdf_path = os.path.join(output_directory, os.path.splitext(filename)[0] + ".pdf")
        agregar_imagenes_pdf(img_fondo_path, img_superior_path1, img_superior_path2, output_pdf_path, yinferior=125, ysuperior=378, error_promedio=errores_promedio[errorpos])
        print(f"Se ha creado el archivo {output_pdf_path}","con error promedio de", errores_promedio[errorpos])
        errorpos += 1 """

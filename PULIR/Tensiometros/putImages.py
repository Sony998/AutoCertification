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
desviaciones = []
certificados = []
errores_list = []
errores_promedio = []
primeras = []
segundas = []   
incertidumbres_expandidas = []
incertidumbres = []
notas = []
fecha = str(df.iat[1, 12])
img_fondo_path1 = "PULIR/Tensiometros/partesReporte/Pagina1.png"
img_fondo_path2 = "PULIR/Tensiometros/partesReporte/Pagina2.png"
img_fondo_path3 = "PULIR/Tensiometros/partesReporte/Pagina3.png"
img_fondo_path4 = "PULIR/Tensiometros/partesReporte/Pagina4.png"
output_directory1 = "PULIR/Tensiometros/Reportes/1"
output_directory2 = "PULIR/Tensiometros/Reportes/2"
output_directory3 = "PULIR/Tensiometros/Reportes/3"
output_directory4 = "PULIR/Tensiometros/Reportes/4"
inferior_directory = "PULIR/Tensiometros/Graficos/Error"
superior_directory = "PULIR/Tensiometros/Graficos/Desviacion"
errorpos = 0
while True:
    if fila_actual >= len(df):
        break
    certficado = df.iat[fila_actual, 7]
    error_promedio = df.iat[fila_actual + 8, 1]
    nota = df.iat[fila_actual + 4, 8]
    if pd.isna(nota):
        nota = "No se realizan observaciones"
    else:
        nota = str(nota)
    desviacion = df.iat[fila_actual + 9, 1]
    primera = df.iloc[fila_actual + 5, 1:7].astype(float).tolist()
    segunda = df.iloc[fila_actual + 6, 1:7].astype(float).tolist()
    incertidumbre = float(df.iat[fila_actual + 11, 1])
    incertidumbres_expandida = float(df.iat[fila_actual + 12, 1])
    errores_promedio.append(error_promedio)
    errores = df.iloc[fila_actual + 7, 1:7].astype(float).tolist()
    primeras.append(primera)
    segundas.append(segunda)
    incertidumbres.append(incertidumbre)
    incertidumbres_expandidas.append(incertidumbres_expandida)
    certificados.append(certficado)
    desviaciones.append(desviacion)
    errores_list.append(errores)
    notas.append(nota)
    print(f"Certificado: {certficado}, Error promedio: {error_promedio}, desviacion {desviacion} nota {nota}")
    fila_actual += 19



def agregar_imagenes_pdf3(img_fondo_path, img_superior_path1, img_superior_path2, output_pdf_path, yinferior, ysuperior, error_promedio, desviacion):
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
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    c.setFont("Arial", 11)
    c.drawString(350, 678, "{:.2f}".format(float(f"{error_promedio:.2f}")))
    c.drawString(350, 659, "{:.2f}".format(float(f"{desviacion:.2f}")))
    c.save()
def agregar_imagenes_pdf1(fondo_path, output_pdf_path, nombrecertificado):
    carta_ancho, carta_alto = letter
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    c.drawImage(fondo_path, 0, 0, width=carta_ancho, height=carta_alto, preserveAspectRatio=True, mask='auto')
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    pdfmetrics.registerFont(TTFont('ArialBold', 'ArialBold.ttf'))
    pdfmetrics.registerFont(TTFont('ArialI', 'ArialI.ttf'))
    c.setFont("ArialI", 14)
    c.drawString(312, 657, nombrecertificado)
    c.setFont("Arial", 15)
    c.drawString(270, 230, "6 de noviembre del 2024")
    c.drawString(270, 195, "7 de noviembre del 2024")
    c.drawString(295, 160, "Cucaita, Boyaca")
    c.drawString(250, 124, "Ingeniera Luz Alejandra Vargas")
    c.save()

""" for certficado in certificados:
    img_superior_path1 = os.path.join(inferior_directory, certficado + ".png")
    img_superior_path2 = os.path.join(superior_directory, certficado + ".png")
    output_pdf_path = os.path.join(output_directory3, certficado + ".pdf")
    agregar_imagenes_pdf3(img_fondo_path, img_superior_path1, img_superior_path2, output_pdf_path, 
                         yinferior=125, ysuperior=378, error_promedio=errores_promedio[errorpos], desviacion=desviaciones[errorpos])
    print(f"Se ha creado el archivo {output_pdf_path}","con error promedio de", errores_promedio[errorpos])
    errorpos += 1 """
def agregar_imagenes_pdf2(fondo_path, output_pdf_path, nombrecertificado, incertidumbre, incertidumbre_expandida, primera, segunda, errores_list):
    carta_ancho, carta_alto = letter
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    c.drawImage(fondo_path, 0, 0, width=carta_ancho, height=carta_alto, preserveAspectRatio=True, mask='auto')
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    pdfmetrics.registerFont(TTFont('ArialBold', 'ArialBold.ttf'))
    pdfmetrics.registerFont(TTFont('ArialI', 'ArialI.ttf'))
    c.setFont("ArialI", 14)
    c.drawString(330, 660, "19")
    c.drawString(398, 660, "20")
    c.drawString(360, 630, "1016")
    c.drawString(330, 600, "60")
    c.drawString(398, 600, "68")
    c.drawString(330, 398, "{:.2f}".format(float(f"{incertidumbre_expandida:.2f}")))
    c.drawString(330, 378, "{:.2f}".format(float(f"{incertidumbre:.2f}")))
    c.setFont("ArialI", 12)
    for i in range(6):
        c.drawString(175 + i * 45+(i*2.7), 135 , "{:.2f}".format(float(f"{primera[i]:.2f}")))
    for i in range(6):
        c.drawString(175 + i * 45+(i*2.7), 105 , "{:.2f}".format(float(f"{segunda[i]:.2f}")))
    for i in range(6):
        c.drawString(175 + i * 50-(i), 77 , "{:.2f}".format(float(f"{errores_list[i]:.2f}")))
    c.save()

""" for certficado, error_promedio, desviacion in zip(certificados, errores_promedio, desviaciones):
    agregar_imagenes_pdf1(img_fondo_path1, os.path.join(output_directory1, certficado + ".pdf"), certficado)
 """
def agregar_imagenes_pdf4(fondo_path, output_pdf_path , nota):
    carta_ancho, carta_alto = letter
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    c.drawImage(fondo_path, 0, 0, width=carta_ancho, height=carta_alto, preserveAspectRatio=True, mask='auto')
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    pdfmetrics.registerFont(TTFont('ArialBold', 'ArialBold.ttf'))
    c.setFont("ArialBold", 14)
    c.drawString(220, 660, "OBSERVACIONES")
    c.setFont("Arial", 12)
    max_length = 75  # Maximum characters per line
    if len(nota) > max_length:
        nota_line1 = nota[:max_length]
        nota_line2 = nota[max_length:]
        c.drawString(63, 630, nota_line1)
        c.drawString(63, 610, nota_line2)
    else:
        c.drawString(63, 630, nota)
    c.save()

""" for certficado, error_promedio, desviacion in zip(certificados, errores_list, desviaciones):
    agregar_imagenes_pdf2(img_fondo_path2, os.path.join(output_directory2, certficado + ".pdf"), certficado, incertidumbres[errorpos], incertidumbres_expandidas[errorpos], primeras[errorpos], segundas[errorpos], errores_list[errorpos])
    errorpos += 1
 """
for certficado, error_promedio, desviacion in zip(certificados, errores_list, desviaciones):
    agregar_imagenes_pdf4(img_fondo_path4, os.path.join(output_directory4, certficado + ".pdf"), notas[errorpos] )
    img_superior_path1 = os.path.join(inferior_directory, certficado + ".png")
    img_superior_path2 = os.path.join(superior_directory, certficado + ".png")
    output_pdf_path = os.path.join(output_directory3, certficado + ".pdf")
    agregar_imagenes_pdf3(img_fondo_path3, img_superior_path1, img_superior_path2, output_pdf_path, 
                         yinferior=125, ysuperior=378, error_promedio=errores_promedio[errorpos], desviacion=desviacion)
    errorpos += 1
    print(f"Se ha creado el archivo {output_pdf_path} con error promedio de {error_promedio}")












""" for filename in os.listdir(inferior_directory):
    if filename in os.listdir(superior_directory):
        img_superior_path1 = os.path.join(inferior_directory, filename)
        img_superior_path2 = os.path.join(superior_directory, filename)
        output_pdf_path = os.path.join(output_directory, os.path.splitext(filename)[0] + ".pdf")
        agregar_imagenes_pdf(img_fondo_path, img_superior_path1, img_superior_path2, output_pdf_path, yinferior=125, ysuperior=378, error_promedio=errores_promedio[errorpos])
        print(f"Se ha creado el archivo {output_pdf_path}","con error promedio de", errores_promedio[errorpos])
        errorpos += 1 """

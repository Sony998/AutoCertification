from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
def agregar_imagenes_pdf(img_fondo_path, img_superior_path1, img_superior_path2, output_pdf_path, yinferior, ysuperior):
    img_fondo = Image.open(img_fondo_path).convert("RGBA")
    image_superior = Image.open(img_superior_path1).convert("RGBA")
    image_inferior = Image.open(img_superior_path2).convert("RGBA")
    carta_ancho, carta_alto = letter
    img_fondo.thumbnail((carta_ancho, carta_alto), Image.LANCZOS)
    fondo_path = "temp_fondo.png"
    img_fondo.save(fondo_path, format="PNG")  # Guardar imagen de fondo temporalmente
    image_superior = image_superior.resize((int(image_superior.width / 4), int(image_superior.height / 4)), Image.LANCZOS)
    image_inferior = image_inferior.resize((int(image_inferior.width / 4), int(image_inferior.height / 4)), Image.LANCZOS)
    x_fondo = (carta_ancho - img_fondo.width) // 2
    xinferior = (carta_ancho - image_superior.width) // 2
    xsuperior = (carta_ancho - image_inferior.width) // 2
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    c.drawImage(fondo_path, x_fondo, (carta_alto - img_fondo.height) // 2, width=img_fondo.width, height=img_fondo.height)
    c.drawImage(img_superior_path1, xinferior,yinferior , width=image_superior.width, height=image_superior.height)
    c.drawImage(img_superior_path2, xsuperior, ysuperior, width=image_inferior.width, height=image_inferior.height)
    c.save()
    print(f"PDF guardado en {output_pdf_path}")

img_fondo_path = "marcaDeAgua.png"         # Ruta de la imagen de fondo
image_superior = r"C:\Users\Raven\Desktop\CODE\PULIR\Tensiometros\Graficos\Error\P030711242420.png"  # Primera imagen superior
image_inferior = r"C:\Users\Raven\Desktop\CODE\PULIR\Tensiometros\Graficos\Desviacion\P030711242420.png"  # Segunda imagen superior
output_direcotry = r"C:\Users\Raven\Desktop\CODE\PULIR\Tensiometros\Reportes"   
inferior_directory = r"C:\Users\Raven\Desktop\CODE\PULIR\Tensiometros\Graficos\Error"
superior_directory = r"C:\Users\Raven\Desktop\CODE\PULIR\Tensiometros\Graficos\Desviacion"  # Directorio de las imágenes
for filename in os.listdir(inferior_directory):
    if filename in os.listdir(superior_directory):
        img_superior_path1 = os.path.join(inferior_directory, filename)
        img_superior_path2 = os.path.join(superior_directory, filename)
        output_pdf_path = os.path.join(output_direcotry, os.path.splitext(filename)[0] + ".pdf")
        agregar_imagenes_pdf(img_fondo_path, img_superior_path1, img_superior_path2, output_pdf_path, yinferior=100, ysuperior=500)
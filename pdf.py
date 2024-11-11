import os
from docx2pdf import convert

# Ruta de la carpeta de entrada
input_folder = "C:\\Users\\USUARIO\\OneDrive\\Desktop\\MONTIORES2.0"

# Ruta de la carpeta de salida
output_folder = "C:\\Users\\USUARIO\\OneDrive\\Desktop\\MONITORESPDFS"

# Convertir los archivos .docx a PDF
convert(input_folder)

# Mover los archivos PDF a la carpeta de salida
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith(".pdf"):
            os.replace(os.path.join(root, file), os.path.join(output_folder, file)) 
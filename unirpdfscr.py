import os
from PyPDF2 import PdfMerger

# Rutas de las dos carpetas con los archivos PDF
carpeta1 = 'C:\\Users\\Raven\\Desktop\\CUCAITA\\Termometros\\CERTIFICADOS'
carpeta2 = 'C:\\Users\\Raven\\Desktop\\CUCAITA\\Termometros\\REPORTES'
carpeta3 = 'C:\\Users\\Raven\\Desktop\\CUCAITA\\Termometros\\COMPLETOS'
# Carpeta donde se guardarán los PDFs unidos
carpeta_destino = '/home/raven/Desktop/'

# Obtener la lista de archivos en ambas carpetas
archivos_carpeta1 = os.listdir(carpeta1)
archivos_carpeta2 = os.listdir(carpeta2)

# Iterar sobre los archivos de la primera carpeta
for archivo in archivos_carpeta1:
    # Crear un objeto PdfMerger
    merger = PdfMerger()
    
    # Abrir el archivo de la primera carpeta
    with open(os.path.join(carpeta1, archivo), 'rb') as file:
        merger.append(file)
    
    # Verificar si el archivo también existe en la segunda carpeta
    if archivo in archivos_carpeta2:
        # Abrir el archivo de la segunda carpeta
        with open(os.path.join(carpeta2, archivo), 'rb') as file:
            merger.append(file)
    
    # Crear el archivo unido en la carpeta destino
    with open(os.path.join(carpeta_destino, archivo), 'wb') as output:
        merger.write(output)
print("Proceso completado. Los PDFs unidos se encuentran en la carpeta destino.")
import os
import PyPDF2

input_folder = "C:\\Users\\Raven\\Desktop\\IMPRIMIR"
output_file = "C:\\Users\\Raven\\Desktop\\Faltantes.pdf"

merger = PyPDF2.PdfMerger()

for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith(".pdf"):
            pdf = PyPDF2.PdfReader(os.path.join(root, file))
            merger.append(pdf)

merger.write(open(output_file, "wb"))
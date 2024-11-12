import os
import PyPDF2
folders = ["/home/raven/CODE/PULIR/Tensiometros/Certificados"] ##"/home/raven/CODE/PULIR/Tensiometros/Completos","/home/raven/CODE/PULIR/Termometros/Completos"]

merger = PyPDF2.PdfMerger()

for folder in folders:
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            merger.append(os.path.join(folder, filename))

output_path = os.path.join("/home/raven/Desktop/", "TENSIOMETROSPORTADA.pdf")
with open(output_path, "wb") as f_out:
    merger.write(f_out)

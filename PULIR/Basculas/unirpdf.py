import os
import PyPDF2

folders = ["PULIR/Basculas/Certificados","PULIR/Basculas/Reportes/1", "PULIR/Basculas/Reportes/2", "PULIR/Basculas/Reportes/3", "PULIR/Basculas/Reportes/4","PULIR/Basculas/Reportes/5"]

merger = PyPDF2.PdfMerger()

pdf_files = {}
for folder in folders:
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            if filename not in pdf_files:
                pdf_files[filename] = []
            pdf_files[filename].append(os.path.join(folder, filename))

# Merge PDFs with the same name
for filename, paths in pdf_files.items():
    for path in paths:
        merger.append(path)
    for filename, paths in pdf_files.items():
        merger = PyPDF2.PdfMerger()
        for path in paths:
            merger.append(path)
        output_path = os.path.join("PULIR/Basculas/Completos", filename)
        with open(output_path, "wb") as f_out:
            merger.write(f_out)
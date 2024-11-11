from PyPDF2 import PdfFileReader

with open("dummy.pdf", "rb") as pdf_file:
    pdf_reader = PdfFileReader(pdf_file)
    num_paginas = pdf_reader.getNumPages()
    print(f"El PDF tiene {num_paginas} páginas.")

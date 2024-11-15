from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["sample.pdf","dummy.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

print('PDF files have merged successfully ')

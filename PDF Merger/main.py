import PyPDF2

pdffiles = ["1.pdf", "2.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdffiles:
    with open(filename, "rb") as pdfFile:
        merger.append(pdfFile)

with open("merged.pdf", "wb") as outputFile:
    merger.write(outputFile)

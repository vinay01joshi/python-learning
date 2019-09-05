import PyPDF2

# Opening File in bynary mode as PdfFile reader need stram in bynary mode
with open("Vinay_Joshi.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("roated.pdf", "wb") as output:
        writer.write(output)

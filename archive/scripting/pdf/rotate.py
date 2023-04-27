import PyPDF2

pdf_filename = "./pdfs/loremipsum.pdf"
with open(pdf_filename, 'rb') as file:
    print(file)
    reader = PyPDF2.PdfFileReader(file)
    print(f"Number of pages: { reader.numPages }")

    # print(reader.getPage(1))

    page = reader.getPage(0)
    page.rotateClockwise(90)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open('./pdfs/rotated.pdf','wb') as new_file:
        writer.write(new_file)

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


print("--------------------------------")

pdf_filename1 = "./pdfs/loremipsum.pdf"
pdf_filename2 = "./pdfs/lotr_wikipedia.pdf"

def pdf_combiner(pdf_list, new_file):
    merger = PyPDF2.PdfFileMerger()

    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)

    merger.write(new_file)

pdf_combiner([pdf_filename1, pdf_filename2], "./pdfs/new_merged.pdf")
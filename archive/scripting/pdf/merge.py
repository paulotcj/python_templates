import PyPDF2

pdf_filename1 = "./pdfs/loremipsum.pdf"
pdf_filename2 = "./pdfs/lotr_wikipedia.pdf"

def pdf_combiner(pdf_list, new_file):
    merger = PyPDF2.PdfFileMerger()

    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)

    merger.write(new_file)

pdf_combiner([pdf_filename1, pdf_filename2], "./pdfs/new_merged.pdf")
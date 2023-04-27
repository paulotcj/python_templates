import PyPDF2

watermark_filename = './pdfs/watermark.pdf'
target_filename = './pdfs/new_merged.pdf'
output_filename = './pdfs/pdf_watermark_applied.pdf'

watermark = PyPDF2.PdfFileReader( open(watermark_filename, 'rb') )
target_pdf = PyPDF2.PdfFileReader( open(target_filename, 'rb') )

output_pdf = PyPDF2.PdfFileWriter()



for i in range(target_pdf.numPages):
    page = target_pdf.getPage(i)

    watermark = PyPDF2.PdfFileReader( open(watermark_filename, 'rb') )

    # page.mergePage(watermark.getPage(0))

    wm_page = watermark.getPage(0)
    wm_page.mergePage(page)

    # output_pdf.addPage(page)
    output_pdf.addPage(wm_page)

    with open( output_filename, 'wb' ) as output_file :
        output_pdf.write(output_file)



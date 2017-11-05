from PyPDF2 import PdfFileReader, PdfFileWriter

#first read fromexisting file
infile = PdfFileReader(open('request.pdf', 'rb'))
outfile = PdfFileWriter()


#The page dimensions are typically 8.5 x 11 inches, but
#we need to convert them into units, which is 612 x 792 point.
#100 point=1.38 inch
outfile.addBlankPage(612, 792)
p = infile.getPage(0)
outfile.addPage(p)

#now we write to new blanl file
with open('myPdf.pdf', 'wb') as f:
	outfile.write(f)
f.close()
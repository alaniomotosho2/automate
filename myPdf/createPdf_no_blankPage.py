from PyPDF2 import PdfFileReader, PdfFileWriter


########## this script ensure that no empty blank page is created#############

#first read fromexisting file
infile = PdfFileReader(open('request.pdf', 'rb'))
output = PdfFileWriter()


for i in range(infile.getNumPages()):
	p = infile.getPage(i)
	if p.getContents():
		output.addPage(p)
with open('myPdf_wo_blank.pdf', 'wb') as f:
	output.write(f)

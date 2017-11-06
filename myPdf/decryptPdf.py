from PyPDF2 import PdfFileWriter, PdfFileReader

fp = open('request.pdf', 'rb')
readerObj = PdfFileReader(fp)

writer = PdfFileWriter()
for page in range(readerObj.numPages):
	writer.addPage(readerObj.getPage(page))
writer.encrypt('123456789')

newfp = open('EncryptExercise.pdf', 'wb')
writer.write(newfp)
newfp.close()
fp.close()
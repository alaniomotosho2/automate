from PyPDF2 import PdfFileReader,PdfFileWriter
fp = open('request.pdf', 'rb')
readerObj = PdfFileReader(fp)

page = readerObj.getPage(0)# we just grab the first page---it is zero based
page.rotateCounterClockwise(90)
writer = PdfFileWriter()
writer.addPage(page)
fw = open('RotatedExercise.pdf', 'wb') # we write the result into diferent output file
writer.write(fw)
fw.close()
fp.close()
from PyPDF2 import PdfFileReader, PdfFileMerger
import os

merger = PdfFileMerger()
#wecall os module and refer to the current directory
#we grab aby file end with pdf and put in list
files = [x for x in os.listdir('.') if x.endswith('.pdf')]

for fname in sorted(files):
	merger.append(PdfFileReader(open(os.path.join('.', fname), 'rb')))

merger.write("output.pdf")
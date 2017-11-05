import PyPDF2
from PyPDF2 import PdfFileReader


pdf = open("request.pdf", 'rb')
readerObj = PdfFileReader(pdf)
#print the object
print("PDF Reader Object is:", readerObj)

#getting basic info by invoking readerObj's method
print("Details of request book")
print("Number of pages:", readerObj.getNumPages())
print("Title:", readerObj.getDocumentInfo().title)
print("Author:", readerObj.getDocumentInfo().author)

#exctsarcting conetent of the pdf file
print("\nReading Page 1")
page = readerObj.getPage(1) #we get just page one here
print(page.extractText())
print("##########################################")
page = readerObj.getPage(2) #getting the second page
print(page.extractText())

#getting the file outlines

print("Book Outline")
for heading in readerObj.getOutlines():
	if type(heading) is not list:
		print(dict(heading).get('/Title'))




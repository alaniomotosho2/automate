from PyPDF2 import PdfFileMerger, PdfFileReader

mergerObj = PdfFileMerger()
fp = open('request.pdf', 'wb')
metadata = {u'/edited':u'ByPdfFileMerger',} # we create metadat to add to pdf file
mergerObj.addMetadata(metadata) #we add to it
mergerObj.write(fp)
fp.close()
# we reopen it here
pdf = open("request.pdf", 'rb')
readerObj = PdfFileReader(pdf)
print("Document Info:", readerObj.getDocumentInfo())
pdf.close()
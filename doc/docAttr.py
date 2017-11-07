import docx
doc = docx.Document('ao.docx')
print("Document Object:", doc)
print("Title of the document:")

print(doc.paragraphs[0].text) # first paragaraph is the title

print("Attributes of the document")
print("Author:", doc.core_properties.author)
print("Date Created:", doc.core_properties.created)
print("Document Revision:", doc.core_properties.revision)
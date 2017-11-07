from docx import Document
document = Document()
document.add_heading('Test Document from Docx', 0)
document.save('testDoc.docx')
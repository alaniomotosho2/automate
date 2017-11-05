import fpdf #install fpdf then import it
from fpdf import FPDF

pdf = FPDF(format='letter') # A3 , A4 , A5 ,Letter,and Legal  are supported as format

#we insert empty page before writing to it
pdf.add_page()
pdf.set_font("Arial", size=12) # we specify font 


#cell is the rectangulaer area that contain the text
#we set the heigth snd width of the cell to 200 x 10
# ln =1 indicate a new line ans align='C' is setting alignment to center
pdf.cell(200, 10, txt="Python request for human!", ln=1,align="C")
pdf.cell(200,10,'Python is fun',0,1,'C')#same here
pdf.output("myReq.pdf")
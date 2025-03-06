from reportlab.pdfgen import canvas

def hello(canvas):
    canvas.drawRightString(400,100,"ss World")
    canvas.line(0,0,595,842)
    
    path = canvas.beginPath()
    path.rect(100,200,150,90)
    canvas.drawPath(path, stroke=1, fill=1, fillMode=None) 

canvas.drawImage(self, image, 20,20, width=None,height=None,mask=None) 


c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()
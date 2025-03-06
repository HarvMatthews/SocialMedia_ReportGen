from reportlab.pdfgen import canvas

def hello(canvas):
    canvas.drawString(450,100,"WHAT IF I DO A REALLU LONG MESSAGE< AND DOES IT GO OFF PAGE?! World")
    canvas.line(0,0,595,842)
    
    path = canvas.beginPath()
    path.rect(100,200,150,90)
    canvas.drawPath(path, stroke=1, fill=1, fillMode=None) 



c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()
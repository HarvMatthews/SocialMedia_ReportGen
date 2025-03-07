from reportlab.pdfgen import canvas
from Images import Find_IG_Profile
from MessageStats import Find_SC_TopMessages

Top5Stats = Find_SC_TopMessages(int(5), 0)
TopMessages = Top5Stats[0]
TopMessages.reverse()
Users_SentM = Top5Stats[1]
Top5Snaps = Find_SC_TopMessages(int(5), 1)
TopSnaps = Top5Snaps[0]
TopSnaps.reverse()
Users_SentS = Top5Snaps[1]


def Display(canvas):
    #---The Main Lines---
    #Horizontal
    canvas.line(600,740,0,740)
    canvas.line(600,500,0,500)
    canvas.line(600,400,0,400)
    #Vertical
    canvas.line(300,740,300,500)

    #---Boxes---:

    #---Images---:



    #---Text---
    #Messages:
    canvas.drawString(10,720, TopMessages[0][0] + " has Sent you " + str(TopMessages[0][1]) + " Messages" )
    canvas.drawString(10,700, TopMessages[1][0] + " has Sent you " + str(TopMessages[1][1]) + " Messages" )
    canvas.drawString(10,680, TopMessages[2][0] + " has Sent you " + str(TopMessages[2][1]) + " Messages" )
    canvas.drawString(10,660, TopMessages[3][0] + " has Sent you " + str(TopMessages[3][1]) + " Messages" )
    canvas.drawString(10,640, TopMessages[4][0] + " has Sent you " + str(TopMessages[4][1]) + " Messages" )
    #Snaps:
    canvas.drawString(10,600, TopSnaps[0][0] + " has Sent you " + str(TopSnaps[0][1]) + " Snaps" )
    canvas.drawString(10,580, TopSnaps[1][0] + " has Sent you " + str(TopSnaps[1][1]) + " Snaps" )
    canvas.drawString(10,560, TopSnaps[2][0] + " has Sent you " + str(TopSnaps[2][1]) + " Snaps" )
    canvas.drawString(10,540, TopSnaps[3][0] + " has Sent you " + str(TopSnaps[3][1]) + " Snaps" )
    canvas.drawString(10,520, TopSnaps[4][0] + " has Sent you " + str(TopSnaps[4][1]) + " Snaps" )
    #Big Numbers Section:
    canvas.drawString(310,675,"Messages Sent")
    canvas.drawString(310,575,"Snaps Sent")

    #Increasing Size
    canvas.setFont("Helvetica", 50)
    canvas.drawString(310,690, str(Users_SentM[1]) )
    canvas.drawString(310,590, str(Users_SentS[1]) )




    #path = canvas.beginPath()
    #path.rect(100,200,150,90)
    #canvas.drawPath(path, stroke=1, fill=1, fillMode=None) 

    image_Path = Find_IG_Profile()
    print(image_Path)
    canvas.drawInlineImage(image_Path, 430,405, width=80,height=90) 


Report = canvas.Canvas("Report.pdf")
Display(Report)
Report.showPage()
Report.save()
from reportlab.pdfgen import canvas
from Images import Find_IG_Profile, Find_SC_Logo, Find_IG_Logo
from MessageStats import Find_SC_TopMessages, SC_TopWords_Filtered, SC_TopWords, Sent_Memes

#Snapchat Data
#Messages
Top5Stats = Find_SC_TopMessages(int(5), 0)
TopMessages = Top5Stats[0]
TopMessages.reverse()
Users_SentM = Top5Stats[1]
#Snaps
Top5Snaps = Find_SC_TopMessages(int(5), 1)
TopSnaps = Top5Snaps[0]
TopSnaps.reverse()
Users_SentS = Top5Snaps[1]
#Top Word
SC_Topwords = SC_TopWords_Filtered(SC_TopWords())
SC_Topwords.reverse()
SC_TopWord = SC_Topwords[0]
#IG Top sender
IG_TopSenders = Sent_Memes()
IG_TopSenders.reverse()
IG_Top_Sender = IG_TopSenders[0]

def Display(canvas):
    #---The Main Lines---
    #Horizontal
    canvas.line(600,740,0,740)
    canvas.line(600,500,0,500)
    canvas.line(600,400,0,400)
    #Vertical
    canvas.line(230,740,230,500)

    #---Boxes---:

    #---Images---:
    canvas.drawInlineImage(Find_IG_Profile(), 430,405, width=80,height=90) 
    #canvas.drawInlineImage(Find_SC_Logo(), 430,405, width=80,height=90) 
    canvas.drawInlineImage(Find_SC_Logo(), 460,750, width=153,height=86) 
    canvas.drawInlineImage(Find_IG_Logo(), 10,405, width=90,height=90) 



    #---Text---
    #Messages:
    canvas.drawString(250,720, TopMessages[0][0] + " has Sent you " + str(TopMessages[0][1]) + " Messages" )
    canvas.drawString(250,700, TopMessages[1][0] + " has Sent you " + str(TopMessages[1][1]) + " Messages" )
    canvas.drawString(250,680, TopMessages[2][0] + " has Sent you " + str(TopMessages[2][1]) + " Messages" )
    canvas.drawString(250,660, TopMessages[3][0] + " has Sent you " + str(TopMessages[3][1]) + " Messages" )
    canvas.drawString(250,640, TopMessages[4][0] + " has Sent you " + str(TopMessages[4][1]) + " Messages" )
    #Snaps:
    canvas.drawString(250,600, TopSnaps[0][0] + " has Sent you " + str(TopSnaps[0][1]) + " Snaps" )
    canvas.drawString(250,580, TopSnaps[1][0] + " has Sent you " + str(TopSnaps[1][1]) + " Snaps" )
    canvas.drawString(250,560, TopSnaps[2][0] + " has Sent you " + str(TopSnaps[2][1]) + " Snaps" )
    canvas.drawString(250,540, TopSnaps[3][0] + " has Sent you " + str(TopSnaps[3][1]) + " Snaps" )
    canvas.drawString(250,520, TopSnaps[4][0] + " has Sent you " + str(TopSnaps[4][1]) + " Snaps" )
    #Most Sent Word
    canvas.drawString(10,760, "Is your most sent word, " + str(SC_TopWord[1]) + " times")
    canvas.drawString(10,675,"Messages Sent")
    canvas.drawString(10,575,"Snaps Sent")
    
    #make bigger
    canvas.setFont("Helvetica", 20)

    #IG top Sender
    canvas.drawString(20,370, "You've Sent " + IG_Top_Sender[0] + " " + str(IG_Top_Sender[1]) + " Memes")




    #Big Numbers Section:

    #Increasing Size
    canvas.setFont("Helvetica", 50)
    canvas.drawString(10,690, str(Users_SentM[1]) ) #Messages Sent Big Number
    canvas.drawString(10,590, str(Users_SentS[1]) ) #Snaps Sent Big Number
    canvas.drawString(10,790,SC_TopWord[0] ) #Most Used wods




    #path = canvas.beginPath()
    #path.rect(100,200,150,90)
    #canvas.drawPath(path, stroke=1, fill=1, fillMode=None) 



Report = canvas.Canvas("Report.pdf")
Display(Report)
Report.showPage()
Report.save()
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics import renderPDF
from BasicInfo import Find_IG_Username
from Images import Find_IG_Profile, Find_SC_Logo, Find_IG_Logo
from MessageStats import Find_SC_TopMessages, SC_TopWords_Filtered, SC_TopWords, Sent_Attachments, IG_Groupchats
from InstagramStats import findBlocked, AmountPeopleWhoDontFollowBack, UnfollowedInWeeks, LikesOverYears

#Snapchat Data
#Messages
Top5Stats = Find_SC_TopMessages(int(6), 0)
TopMessages = Top5Stats[0]
TopMessages.reverse()
Users_SentM = Top5Stats[1]

#To remove the top person uncomment line below
del TopMessages[0]

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
IG_TopSenders = Sent_Attachments()
IG_TopSenders.reverse()
IG_Top_Sender = IG_TopSenders[0]

#IG How Many People Unfollowed In weeks
UnfollowedStats = UnfollowedInWeeks()
PeopleUnfollowed = UnfollowedStats[0]
InHowManyWeeks = UnfollowedStats[1]

#Likes Over Years Stats
LikesOverYearsStats = LikesOverYears()
AllLikes = LikesOverYearsStats[0]
YearsArray = LikesOverYearsStats[1]
DataArray = LikesOverYearsStats[2]

moveDown = + 90


def Display(canvas):
    
    # ---The Main Lines---
    #Horizontal
    canvas.line(600,750,0,750)
    
    canvas.line(600,650,0,650)
    canvas.line(600,365,0,365)

    canvas.line(600,310-45,0,310-45)
    #Vertical
    canvas.line(170,605+45,170,325+45)

    # ---Boxes---:

    # ---Images---:
    canvas.drawInlineImage(Find_IG_Profile(), 430,315-45, width=80,height=90) 
    #canvas.drawInlineImage(Find_SC_Logo(), 430,405, width=80,height=90) 
    canvas.drawInlineImage(Find_SC_Logo(), 460,660, width=153,height=86) 
    canvas.drawInlineImage(Find_IG_Logo(), 10,315-45, width=90,height=90) 

    #The Header Section
    name = Find_IG_Username()[1]
    #print(name[1])
    canvas.setFont("Helvetica", 30)
    WelcomeMessage = name + "'s Social Media Report"
    canvas.drawString(10,812, WelcomeMessage)
    canvas.setFont("Helvetica", 12)
    canvas.drawString(10,790, "Little Summary of some Statistics from " + name + "'s Instagram and Snapchat data.") 
    canvas.drawString(10,775, "*All Snapchat Data is only what is saved in Chat")
    canvas.drawString(10,760, "https://github.com/HarvMatthews/SocialMedia_ReportGen")

    
    # Snapchat Section:
    #Messages:
    canvas.setFont("Helvetica", 12)

    canvas.drawString(190,630, TopMessages[0][0] + " has Sent you " + str(TopMessages[0][1]) + " Messages" )
    canvas.drawString(190,610, TopMessages[1][0] + " has Sent you " + str(TopMessages[1][1]) + " Messages" )
    canvas.drawString(190,590, TopMessages[2][0] + " has Sent you " + str(TopMessages[2][1]) + " Messages" )
    canvas.drawString(190,570, TopMessages[3][0] + " has Sent you " + str(TopMessages[3][1]) + " Messages" )
    canvas.drawString(190,550, TopMessages[4][0] + " has Sent you " + str(TopMessages[4][1]) + " Messages" )
    
    # -- The Pie Chart ---
    #The Messages
    renderPDF.draw(makeThePie((TopMessages[0][1],TopMessages[1][1],TopMessages[2][1],TopMessages[3][1],TopMessages[4][1]),(TopMessages[0][0],TopMessages[1][0],TopMessages[2][0],TopMessages[3][0],TopMessages[4][0])), canvas, 432, 495)
    #The Snaps
    renderPDF.draw(makeThePie((TopSnaps[0][1],TopSnaps[1][1],TopSnaps[2][1],TopSnaps[3][1],TopSnaps[4][1]),(TopSnaps[0][0],TopSnaps[1][0],TopSnaps[2][0],TopSnaps[3][0],TopSnaps[4][0])), canvas, 430, 385)

    #Snaps:
    canvas.drawString(190,510-45, TopSnaps[0][0] + " has Sent you " + str(TopSnaps[0][1]) + " Snaps" )
    canvas.drawString(190,490-45, TopSnaps[1][0] + " has Sent you " + str(TopSnaps[1][1]) + " Snaps" )
    canvas.drawString(190,470-45, TopSnaps[2][0] + " has Sent you " + str(TopSnaps[2][1]) + " Snaps" )
    canvas.drawString(190,450-45, TopSnaps[3][0] + " has Sent you " + str(TopSnaps[3][1]) + " Snaps" )
    canvas.drawString(190,430-45, TopSnaps[4][0] + " has Sent you " + str(TopSnaps[4][1]) + " Snaps" )
    #Most Sent Word
    canvas.drawString(10,670, "Is your most Frequently used word at " + str(SC_TopWord[1]) + " times")
    
    #Left Side of Snapchat Section
    canvas.drawString(10,585,"Messages Sent")
    canvas.drawString(10,485,"Snaps Sent")
    
    canvas.setFont("Helvetica", 50)
    canvas.drawString(10,700,SC_TopWord[0] ) #Most Used wods
    canvas.drawString(10,600, str(Users_SentM[1]) ) #Messages Sent Big Number
    canvas.drawString(10,500, str(Users_SentS[1]) ) #Snaps Sent Big Number

    # ---- Instagram Section -----

    canvas.setFont("Helvetica", 20)
    #IG top Sender
    canvas.drawString(20,280-45, "You've Sent " + IG_Top_Sender[0] + " " + str(IG_Top_Sender[1]) + " Attachments")
    canvas.drawString(300,245-45, "You've Blocked " + str(findBlocked()) + " People")
    canvas.drawString(20,210-45, str(AmountPeopleWhoDontFollowBack()) +  " Accounts Don't Follow you back ")
    canvas.drawString(200,180-45, "Unfollowed " + str(PeopleUnfollowed) +  " People In the past " + str(InHowManyWeeks) + " weeks")

    canvas.drawString(250,50,"Group Chats")


    #Increasing Size
    canvas.setFont("Helvetica", 50)
    canvas.drawString(250,70, "In " + str(IG_Groupchats())) #Group Chats
    
    #Bar Chart
    canvas.setFont("Helvetica", 10)

    renderPDF.draw(MakeTheBar(),canvas,30,40)
    canvas.drawString(30,15, "Amount Of Likes Given in Years")


    #path = canvas.beginPath()
    #path.rect(100,200,150,90)
    #canvas.drawPath(path, stroke=1, fill=1, fillMode=None) 


def makeThePie(data, label):
    theDrawingOfPie = Drawing(80,80)
    thePie = Pie()
    thePie.x = 0
    thePie.y = 0
    thePie.width = 80
    thePie.height = 80
    thePie.data = data
    thePie.labels = label
    thePie.sideLabels = True
    thePie.simpleLabels = 0
    theDrawingOfPie.add(thePie)
    return theDrawingOfPie

from reportlab.graphics.charts.barcharts import VerticalBarChart
 
def MakeTheBar():
    theBar = VerticalBarChart()

    theBar.x = 0
    theBar.y = 0
    theBar.width = 220
    theBar.height = 110

    theBar.data = [DataArray]
    theBar.categoryAxis.categoryNames = YearsArray
    
    theBarAsDrawing = Drawing(220,110)
    theBarAsDrawing.add(theBar)
    return theBarAsDrawing



Report = canvas.Canvas("Report.pdf")
Display(Report)
Report.showPage()
Report.save()
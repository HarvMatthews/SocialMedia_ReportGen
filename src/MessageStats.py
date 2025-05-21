import os
import json
import operator
from src.BasicInfo import Find_SC_Username, Find_IG_Username
from src.theLocations import SC_Chat_History_JSON, SC_Snap_History_JSON, IG_Messages_File


#I could have TopMessages and Top people in one loop where I have a variable of like chats["Friends"] and chats["Contents"]
#But I purposely have them as different functions because in future I want to be able to call the data differently

'''
If the type is 0 then will be Text messages
if the type is 1, then will be snap messages

FindTop5Messages()
Returns a tuple with the 
first being an array of tuples of top messages (Username, Amount of messages)
second being the users own stats (Username, amount of messages)
'''
def Find_SC_TopMessages(Amount: int, Type: int):
    if Type == 0:
        Chats_Dir =  SC_Chat_History_JSON()
    elif Type == 1:
        Chats_Dir =  SC_Snap_History_JSON()

    with open(Chats_Dir) as file:
        json_data = json.load(file)

    Keys = json_data.keys()
    #Keys being either the gc code or the pm

    MessagesDict = {}
    for key in Keys:
        Chat_History = json_data[key]
        
        for chats in Chat_History:
            SearchingUser = chats["From"]

            if SearchingUser not in MessagesDict:
                MessagesDict[SearchingUser] = 0

            MessagesDict[SearchingUser] += 1

        
    #Removing the users own sent messages:

    FindUser = Find_SC_Username() #So its not calling the fun every iteration
    UserSent = None
    Messages_Sorted_Filtered = []
    Messages_Sorted = sorted(MessagesDict.items(), key=operator.itemgetter(1))
    for people in Messages_Sorted:
        if people[0] == FindUser:
            UserSent = (people[0],people[1])
        else:
            Messages_Sorted_Filtered.append(people)
    
    Top_Amount = Messages_Sorted_Filtered[((len(Messages_Sorted_Filtered)) - Amount):] #top 5
    #print(UserSent)
    #print(Top5)
    return(Top_Amount, UserSent)

def SC_TopWords():
    Chats_Dir =  SC_Chat_History_JSON()
    
    with open(Chats_Dir) as file:
        json_data = json.load(file)

    Keys = json_data.keys()
    #Keys being either the gc code or the pm

    WordsDict = {}
    for key in Keys:
        Chat_History = json_data[key]
        for chats in Chat_History:
            #if chats["From"] == Findusername():
            #Only messages that have been sent from the users account
            Content = chats["Content"]
            
            if type(Content) == str:
                indivWords = Content.split(" ")

                
                for word in indivWords:
                    word = word.lower()
                    #Adding the words to dict
                    if word not in WordsDict:
                        WordsDict[word] = 0
                    #Couting the words whilst being added
                    WordsDict[word] += 1
        
    Words_Sorted = sorted(WordsDict.items(), key=operator.itemgetter(1))
    return(Words_Sorted)

def SC_TopWords_Filtered(TopWords):
    filler_words = [
    'I', 'you', 'he', 'she', 'it', 'we', 'they',  
    'the', 'a', 'an', 'that', 'this', 'there',  
    'is', 'are', 'was', 'were', 'to', 'of', 'in',  
    'and', 'but', 'or', 'so', 'then', 'just',  
    'like', '', ' ', 'i', 'for'
]
    
    Words_Filtered = []
    for Word in TopWords:
        if Word[0] not in filler_words:
            Words_Filtered.append(Word)
    return(Words_Filtered)

def IG_DM_Files():
    #If content contains word "Attachment" AND Sender == Users
    File_Dirs = []
    Messages_Dir = IG_Messages_File()
    
    items = os.listdir(Messages_Dir)
    for MessageFile in items:
        if MessageFile.find(".") == -1:
            JsonFile = Messages_Dir + "/" + MessageFile + "/message_1.json"
            File_Dirs.append(JsonFile)
        
    return(File_Dirs)

def IG_Groupchats():
    Amount_GC = 0
    for jsonFile in IG_DM_Files():
        with open(jsonFile) as file:
                json_data = json.load(file)
                participants = json_data["participants"]
                if(len(participants) > 2):
                    Amount_GC += 1
                
    return(Amount_GC)

def Sent_Attachments():
    AllPeople = {}
    for jsonFile in IG_DM_Files():
        Sent = 0
        with open(jsonFile) as file:
                json_data = json.load(file)
                participants = json_data["participants"]
                if(len(participants) <= 2):
                    #Process here
                    for message in json_data["messages"]:
                        if message["sender_name"] == Find_IG_Username()[1]:
                            content = message.get("content")
                            if content is not None:
                                if "attachment" in content:
                                    Sent += 1
                    if Sent > 0:
                        AllPeople[(participants[0]["name"])] = Sent
                        #AllPeople.append(((participants[0]["name"]), (Sent)))
                        
    people_sorted = sorted(AllPeople.items(), key=operator.itemgetter(1))
    return(people_sorted)

#TopSenders = Sent_Attachments()
#TopSenders.reverse()
#print(TopSenders[0])

import json
import operator
from BasicInfo import Findusername, FindDir


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
def FindTopMessages(Amount: int, Type: int):
    if Type == 0:
        Chats_Dir =  FindDir() +  "/json/chat_history.json"
    elif Type == 1:
        Chats_Dir =  FindDir() +  "/json/snap_history.json"

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

    FindUser = Findusername() #So its not calling the fun every iteration
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






def TopWords():
    Chats_Dir =  FindDir() +  "/json/chat_history.json"
    
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

def TopWords_Filtered(TopWords):
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



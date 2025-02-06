import os
import json
import operator


'''
If the type is 0 then will be Text messages
if the type is 1, then will be snap messages

FindTop5Messages()
Returns a tuple with the 
first being an array of tuples of top messages (Username, Amount of messages)
second being the users own stats (Username, amount of messages)
'''
def FindTopMessages(Amount: int, Type: int):
    from BasicInfo import Findusername, FindDir
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
    
    Top5 = Messages_Sorted_Filtered[((len(Messages_Sorted_Filtered)) - Amount):] #top 5
    #print(UserSent)
    #print(Top5)
    return(Top5, UserSent)
                

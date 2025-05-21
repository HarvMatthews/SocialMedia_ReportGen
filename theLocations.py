import os

pathOfWhole = os.path.dirname(os.path.abspath(__file__))


theDirOfData = os.path.join(pathOfWhole, "DataInsideHere")
print(theDirOfData)

#Snapchat

def Find_SC_Dir():
    SCDir = os.path.join(theDirOfData,"json")
    return SCDir

def SC_Account_JSON():
    SC_Account_JSON = os.path.join(theDirOfData, "json/account.json")
    return SC_Account_JSON


#Instagram


def Find_Instagram_Dir():
    items = os.listdir(theDirOfData)
    for item in items:
        if (item.find('.') == -1) and (item != "json"): #(Ensures is a folder) AND (Not json)
            Instagram_Dir = theDirOfData + "/" + item
            return(Instagram_Dir)

def Find_IG_PersonalInfo_JSON():
    Find_IG_PersonalInfo_JSON = os.path.join(Find_Instagram_Dir(), "personal_information/personal_Information/personal_information.json")
    return Find_IG_PersonalInfo_JSON

def IG_Friends_Folder():
    IG_Friends_Folder = os.path.join(Find_Instagram_Dir(),"connections/followers_and_following")
    return IG_Friends_Folder

import os

#This File has all the paths needed throughout the project
#If SC or IG change the layout of the JSON file, this file updates
Path_Of_Here = os.path.dirname(os.path.abspath(__file__))
Path_Of_Project = os.path.dirname(os.path.abspath(Path_Of_Here))
print(Path_Of_Project)
theDirOfData = os.path.join(Path_Of_Project, "DataInsideHere")


#Snapchat Paths

def Find_SC_Dir():
    SCDir = os.path.join(theDirOfData,"json")
    return SCDir

SC_Dir = Find_SC_Dir()

def SC_Account_JSON():
    SC_Account_JSON = os.path.join(SC_Dir, "account.json")
    return SC_Account_JSON

def SC_Chat_History_JSON():
    SC_Chat_History_JSON = os.path.join(SC_Dir,"chat_history.json")
    return SC_Chat_History_JSON

def SC_Snap_History_JSON():
    SC_Snap_History_JSON = os.path.join(SC_Dir,"snap_history.json")
    return SC_Snap_History_JSON


#Instagram Paths

def Find_Instagram_Dir():
    items = os.listdir(theDirOfData)
    for item in items:
        if (item.find('.') == -1) and (item != "json"): #(Ensures is a folder) AND (Not json)
            Instagram_Dir = theDirOfData + "/" + item
            return(Instagram_Dir)
        
def IG_Friends_Folder():
    IG_Friends_Folder = os.path.join(Instagram_Dir,"connections/followers_and_following")
    return IG_Friends_Folder

#This is so its not calling the function multiple times
Instagram_Dir = Find_Instagram_Dir()
FriendsFolder = IG_Friends_Folder()

def IG_LikedPost_JSON():
    IG_LikedPost_JSON = os.path.join(Instagram_Dir,"your_instagram_activity/likes/liked_posts.json")
    return IG_LikedPost_JSON

def Find_IG_PersonalInfo_JSON():
    Find_IG_PersonalInfo_JSON = os.path.join(Instagram_Dir, "personal_information/personal_Information/personal_information.json")
    return Find_IG_PersonalInfo_JSON

def IG_Blocked_Profiles_JSON():
    IG_Blocked_Profiles_JSON = os.path.join(FriendsFolder, "blocked_profiles.json")
    return IG_Blocked_Profiles_JSON

def IG_Followers_JSON():
    IG_Followers_JSON = os.path.join(FriendsFolder, "followers_1.json")
    return IG_Followers_JSON

def IG_Following_JSON():
    IG_Following_JSON = os.path.join(FriendsFolder, "following.json")
    return IG_Following_JSON

def IG_Unfollowed_Profiles_JSON():
    IG_Unfollowed_Profiles_JSON = os.path.join(FriendsFolder,"recently_unfollowed_profiles.json")
    return IG_Unfollowed_Profiles_JSON

def IG_Messages_File():
    IG_Messages_File = os.path.join(Instagram_Dir,"your_instagram_activity/messages/inbox")
    return IG_Messages_File




def IG_Profile():
    IG_Profile = os.path.join(Instagram_Dir,"media/profile")
    return IG_Profile

def ImageLoc():
    ImageLoc = os.path.join(Path_Of_Project,"assests/images")
    return ImageLoc

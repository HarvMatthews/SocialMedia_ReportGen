import os
import json
from BasicInfo import Find_SC_Username, Find_Dir, Find_Instagram_Dir, Find_IG_Username

friendsFolder = Find_Instagram_Dir() + "/connections/followers_and_following"

def findBlocked():
    blockedInfo = friendsFolder + "/blocked_profiles.json"
    with open(blockedInfo) as file:
        json_data = json.load(file)
        blocked = json_data["relationships_blocked_users"]
        #print(blocked)
        amountBlocked = len(blocked)
        return(amountBlocked)
    
#print(findBlocked())

def AmountPeopleWhoDontFollowBack():
    followersDir = friendsFolder + "/followers_1.json"
    followingDir = friendsFolder + "/following.json"
    followers = []
    followingList = []
    PeopleWhoDontFollowBack = []

    with open(followersDir) as followersFile:
        followersData = json.load(followersFile)
    
    with open(followingDir) as followingFile:
        followingData = json.load(followingFile)

    for follower in followersData:
        #print(follower)
        followerName = follower["string_list_data"][0]["value"]
        followers.append(followerName)
    
    #print(followingData)
    for following in followingData["relationships_following"]:
        followingName = following["string_list_data"][0]["value"]
        followingList.append(followingName)

    for CompareFollowing in followingList:
        if CompareFollowing not in followers:
            PeopleWhoDontFollowBack.append(CompareFollowing)

    
    return len(PeopleWhoDontFollowBack)


print(AmountPeopleWhoDontFollowBack())





    

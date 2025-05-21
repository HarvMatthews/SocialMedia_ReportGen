import time
import datetime
import json
from BasicInfo import Find_SC_Username, Find_Dir, Find_IG_Username
from theLocations import Find_Instagram_Dir, IG_Friends_Folder

friendsFolder = IG_Friends_Folder()

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

def UnfollowedInWeeks():
    UnfollowedDir = friendsFolder + "/recently_unfollowed_profiles.json"
    with open(UnfollowedDir) as file:
        json_data = json.load(file)
        unfollowed = json_data["relationships_unfollowed_users"]
        listOfTimes = []
        AmmountUnfollowed = len(unfollowed)
        #print(len(unfollowed))
        for IndivUnfollowed in unfollowed:
            timeStamp = IndivUnfollowed["string_list_data"][0]["timestamp"]
            #print(IndivUnfollowed["string_list_data"][0]["timestamp"])
            listOfTimes.append(timeStamp)

        #Convert to weeks ago
        longAgoEpoch = (time.time()) - min(listOfTimes)
        weeksAgo = int(longAgoEpoch / (7 * 24 * 60 * 60))
        print(weeksAgo)

    return((AmmountUnfollowed,weeksAgo))

#Returns Tuble(Int, Dict["Year":int])
def LikesOverYears():
    likesDir = Find_Instagram_Dir() + "/your_instagram_activity/likes/liked_posts.json"
    with open(likesDir) as file:
        json_data = json.load(file)
        allLikes = json_data["likes_media_likes"]
        yearLikesDict = {}
        amountOfLikes = len(allLikes)
        #print(amountOfLikes)
        for indivLikes in allLikes:
            timeStamp = indivLikes["string_list_data"][0]["timestamp"]
            theYear = datetime.datetime.fromtimestamp(timeStamp).year
            #print(theYear)
            if theYear not in yearLikesDict:
                yearLikesDict[theYear] = 0
            yearLikesDict[theYear] += 1

        data = []
        YearsArray = []
        for Years in yearLikesDict:
            YearsArray.append(str(Years))
            data.append(yearLikesDict[Years])
  

    return([amountOfLikes, YearsArray, data])

LikesOverYears()




    

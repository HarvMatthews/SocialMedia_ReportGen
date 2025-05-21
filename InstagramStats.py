import time
import datetime
import json
from BasicInfo import Find_SC_Username, Find_Dir, Find_IG_Username
from theLocations import Find_Instagram_Dir, IG_Friends_Folder, IG_Blocked_Profiles_JSON, IG_Followers_JSON, IG_Following_JSON, IG_Unfollowed_Profiles_JSON, IG_LikedPost_JSON

friendsFolder = IG_Friends_Folder()

def findBlocked():
    with open(IG_Blocked_Profiles_JSON()) as file:
        json_data = json.load(file)
        blocked = json_data["relationships_blocked_users"]
        #print(blocked)
        amountBlocked = len(blocked)
        return(amountBlocked)
    
#print(findBlocked())

def AmountPeopleWhoDontFollowBack():
    followers = []
    followingList = []
    PeopleWhoDontFollowBack = []

    with open(IG_Followers_JSON()) as followersFile:
        followersData = json.load(followersFile)
    
    with open(IG_Following_JSON()) as followingFile:
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
    with open(IG_Unfollowed_Profiles_JSON()) as file:
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
    with open(IG_LikedPost_JSON()) as file:
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




    

import os
import json
from BasicInfo import Find_Instagram_Dir

#Get Profile Pictiures/Random image from snapchat
Images_Dir = Find_Instagram_Dir() + "/media/profile"
Possible_Pics = os.listdir(Images_Dir)
Profile_Pic_Dir = Possible_Pics[0]
print(Profile_Pic_Dir)


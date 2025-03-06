import os
import json
from BasicInfo import FindDir

#Get Profile Pictiures/Random image from snapchat
Images_Dir = Find_SC_Dir() + ""

with open(Images_Dir) as file:
        json_data = json.load(file)

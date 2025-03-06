import os
import json
from BasicInfo import FindDir

#Get Profile Pictiures/Random image from snapchat
Images_Dir = FindDir() + ""

with open(Images_Dir) as file:
        json_data = json.load(file)

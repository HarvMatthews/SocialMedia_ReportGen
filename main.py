import os
from src.Display import Generate


if 'DataInsideHere' not in os.listdir():
    print("Missing Folder")
    quit()

theDataInside = os.listdir("DataInsideHere")
if len(theDataInside) < 2:
    print("Missing Data")
    quit()

if "json" not in theDataInside:
    print("Missing Snapchat JSON File")
    quit()


Does_IG_Exist = False
for files in theDataInside:
    if files.startswith("instagram"):
        Does_IG_Exist = True

if not Does_IG_Exist:
    print("Instagram Data Missing")
    quit()

Generate()






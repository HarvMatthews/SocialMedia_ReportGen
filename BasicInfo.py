import os
import json

def FindDir():
    return(os.path.dirname(os.path.abspath(__file__)))

def Findusername():
    with open(FindDir()+  "/json/account.json") as file:
        json_data = json.load(file)
    return(json_data["Basic Information"]["Username"])
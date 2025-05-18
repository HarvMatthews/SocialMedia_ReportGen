import os
import json

def Find_Dir():
    Dir = os.path.dirname(os.path.abspath(__file__)) + "/DataInsideHere"
    return (Dir)

def Find_SC_Dir():
    Find_Dir() + "/json"

def Find_Instagram_Dir():
    items = os.listdir(Find_Dir())
    for item in items:
        if (item.find('.') == -1) and (item != "json"): #(Ensures is a folder) AND (Not json)
            Instagram_Dir = Find_Dir() + "/" + item
            return(Instagram_Dir)

def Find_SC_Username():
    with open(Find_Dir()+  "/json/account.json") as file:
        json_data = json.load(file)
    return(json_data["Basic Information"]["Username"])

def Find_IG_Username():
    FileDir = Find_Instagram_Dir() + "/personal_information/personal_Information/personal_information.json"
    with open(FileDir) as file:
        json_data = json.load(file)
        Username = json_data["profile_user"][0]["string_map_data"]["Username"]["value"]
        Name = json_data["profile_user"][0]["string_map_data"]["Name"]["value"]
        return((Username, Name))
import os
import json
from src.theLocations import SC_Account_JSON, Find_IG_PersonalInfo_JSON

def Find_Dir():
    Dir = os.path.dirname(os.path.abspath(__file__)) + "/DataInsideHere"
    return (Dir)


def Find_SC_Username():
    with open(SC_Account_JSON()) as file:
        json_data = json.load(file)
    return(json_data["Basic Information"]["Username"])

def Find_IG_Username():
    with open(Find_IG_PersonalInfo_JSON()) as file:
        json_data = json.load(file)
        Username = json_data["profile_user"][0]["string_map_data"]["Username"]["value"]
        Name = json_data["profile_user"][0]["string_map_data"]["Name"]["value"]
        return((Username, Name))
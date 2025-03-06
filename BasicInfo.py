import os
import json

def Find_SC_Dir():
    SC_Dir = os.path.dirname(os.path.abspath(__file__)) + "/DataInsideHere"
    return(SC_Dir)

def Find_SC_Username():
    with open(Find_SC_Dir()+  "/json/account.json") as file:
        json_data = json.load(file)
    return(json_data["Basic Information"]["Username"])

def Find_Instagram_Dir():
    data_inside_here = Find_SC_Dir() + "/DataInsideHere"
    items = os.listdir(data_inside_here)
    for item in items:
        if (item.find('.') == -1) and (item != "json"): #(Ensures is a folder) AND (Not json)
            #print("   " + item)
            return(item)
    

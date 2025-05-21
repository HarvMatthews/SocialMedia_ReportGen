import os
from theLocations import IG_Profile, ImageLoc

def Find_IG_Profile():
        #Get Profile Pictiures/Random image from snapchat
        Images_Dir = IG_Profile()

        #The folder name can be different per person
        for File in os.listdir(Images_Dir):
                if File.find('.') == -1:
                        Profile_Pic_Dir = Images_Dir + "/" + File
        
        for Image in os.listdir(Profile_Pic_Dir):
                if Image.endswith(".jpg"):
                        #print(Image)
                        Profile_Pic_Dir = Profile_Pic_Dir + "/" + Image
        
        #print(Profile_Pic_Dir)

        return(Profile_Pic_Dir)

def Find_SC_Logo():
        SC_Logo = os.path.join(ImageLoc(),"Snapchat_Logo.jpg")
        return(SC_Logo)

def Find_IG_Logo():
        IG_Logo = os.path.join(ImageLoc(),"Instagram_logo.jpg")
        return(IG_Logo)


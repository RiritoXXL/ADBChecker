import pathlib

class ADB:
    def CheckIfADBIsInstalled():
        if(pathlib.Path("C:\\Program Files\\ADB").is_dir()) == False:
            print("This ADB(Android Debug Bridge) is not installed... Please Install ADB!!!")
        else:
            print("ADB Is Installed!!!")
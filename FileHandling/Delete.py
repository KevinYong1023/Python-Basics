import os
deleteFile = "C:/Users/Kevin/Desktop/DemoPython.txt"
os.remove(deleteFile)
if os.path.exists(deleteFile):
    print("Please delete it")
else:
    print("File does not exist")

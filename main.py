import os
import random

########################################################

def createMaze():
    b = "0123456789abcdef"
    bLen = len(b)
    pathLen = 3
    
    print("\nFirst of all, check that your file is in the 'file' folder\n")
    folderName = input("Name of the folder: ") #"FOLDMAZE"
    path = "newFolders/"+folderName+"/"
    os.mkdir(path)

    fileName = "".join(x for x in os.listdir("file") if x!="example.txt")

    myPath = path
    for x in range(pathLen):
        myPath += random.choice(b)+"/"

    for x in range(bLen):
        os.mkdir(path+b[x]) # path/a
        for y in range(bLen):
            os.mkdir(path+b[x]+"/"+b[y])
            for z in range(bLen):
                os.mkdir(path+b[x]+"/"+b[y]+"/"+b[z])

    os.replace("file/"+fileName, myPath+fileName)
    print("File path: "+myPath+fileName)

########################################################

createMaze()
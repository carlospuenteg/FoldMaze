import os
import random

########################################################

b = "0123456789abcdef"
bLen = len(b)
foldName = "FOLDMAZE"
path = "newFolders/"+foldName+"/"

os.mkdir(path)

fileName = "myGit.txt"
fileContent = "https://github.com/Fisherman386"

strLen = 3

myPath = path
for x in range(strLen):
    myPath += random.choice(b)+"/"

for x in range(bLen):
    os.mkdir(path+b[x]) # path/a
    for y in range(bLen):
        os.mkdir(path+b[x]+"/"+b[y])
        for z in range(bLen):
            os.mkdir(path+b[x]+"/"+b[y]+"/"+b[z])

f = open(myPath+fileName, "x")
f.write(fileContent)

print(myPath+fileName)
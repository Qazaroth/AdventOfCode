import os

inpFile = open("input.txt", "r")
rawData = inpFile.read()
rawDataList = rawData.splitlines()

outList = []

sumNum = 0
for i in rawDataList:
    if i:
        sumNum += int(i)
    else:
        outList.append(sumNum)
        sumNum = 0

outList.sort()

sumOfTopThree = 0

for i in range(-1, -4, -1):
    sumOfTopThree += outList[i]

# First part
print(outList)

# Second part
print(sumOfTopThree)
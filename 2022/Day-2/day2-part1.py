paper = ["B", "Y", 2]
rock = ["A", "X", 1]
scissor = ["C", "Z", 3]

winScore = 6
loseScore = 0
drawScore = 3

strategyFile = open("input.txt", "r")
stratFileData = strategyFile.read().splitlines()

def isValid(choice):
    return choice in paper or choice in rock or choice in scissor

def givePoint(data : str):
    dataList = data.split()

    enemyChoice = dataList[0]
    plrChoice = dataList[1]

    if isValid(enemyChoice) and isValid(plrChoice):
        if plrChoice in rock and enemyChoice in rock:
            return drawScore + rock[-1]
        elif plrChoice in paper and enemyChoice in paper:
            return drawScore + paper[-1]
        elif plrChoice in scissor and enemyChoice in scissor:
            return drawScore + scissor[-1]
        
        if enemyChoice in rock:
            if plrChoice in paper:
                return winScore + paper[-1]
            elif plrChoice in scissor:
                return loseScore + scissor[-1]
        elif enemyChoice in paper:
            if plrChoice in scissor:
                return winScore + scissor[-1]
            elif plrChoice in rock:
                return loseScore + rock[-1]
        elif enemyChoice in scissor:
            if plrChoice in rock:
                return winScore + rock[-1]
            elif plrChoice in paper:
                return loseScore + paper[-1]
                
pointsTotal = 0
for i in stratFileData:
    pointsTotal += givePoint(i)

print(pointsTotal)
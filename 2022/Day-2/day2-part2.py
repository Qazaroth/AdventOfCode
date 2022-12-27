rock = ["A", 1]
paper = ["B", 2]
scissor = ["C", 3]

plrLose = ["X", 0]
plrDraw = ["Y", 3]
plrWin = ["Z", 6]

strategyFile = open("input.txt", "r")
stratFileData = strategyFile.read().splitlines()

def isValid(choice):
    return choice in paper or choice in rock or choice in scissor

def whatPlrNeedsToChoose(enemyChoice, outcome):
    if outcome in plrDraw:
        if enemyChoice in rock:
            return rock
        elif enemyChoice in paper:
            return paper
        else:
            return scissor

    if outcome in plrWin:
        if enemyChoice in rock:
            return paper
        elif enemyChoice in paper:
            return scissor
        else:
            return rock

    if outcome in plrLose:
        if enemyChoice in rock:
            return scissor
        elif enemyChoice in scissor:
            return paper
        else:
            return rock

totalPoint = 0
for i in stratFileData:
    data = i.split()
    print(data)

    enemyChoice = data[0]
    outcome = data[1]

    plrChoice = whatPlrNeedsToChoose(enemyChoice, outcome)
    newPoint = plrChoice[-1]
    
    if outcome in plrWin:
        newPoint += plrWin[-1]
    elif outcome in plrDraw:
        newPoint += plrDraw[-1]
    elif outcome in plrLose:
        newPoint += plrLose[-1]
    
    totalPoint += newPoint

print(totalPoint)
inputFile = open("input.txt", "r")
inputFileData = inputFile.read().splitlines()

def isSubset(l1, l2):
    flag1 = False
    flag2 = False

    if (all(x in l1 for x in l2)): flag1 = True
    if (all(x in l2 for x in l1)): flag2 = True

    return flag1 or flag2

def getSections(list: str):
    boundaries = list.split("-")
    boundary1 = int(boundaries[0])
    boundary2 = int(boundaries[-1])

    sections = []
    
    for i in range(boundary1, boundary2 + 1):
        sections.append(i)

    return sections

fullyContained = 0
for pair in inputFileData:
    pairs = pair.split(",")

    firstElf = getSections(pairs[0])
    secondElf = getSections(pairs[1])
    
    if isSubset(firstElf, secondElf):
        fullyContained += 1

print(fullyContained)
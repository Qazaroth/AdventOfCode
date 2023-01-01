import string

alphabets = list(string.ascii_lowercase) + list(string.ascii_uppercase)

inputFile = open("input.txt", "r")
inputFileData = inputFile.read().splitlines()

fileData = [inputFileData[x:x+3] for x in range(0, len(inputFileData), 3)]
badges = []

def commonCharacter(a=[]):
    if len(a) == 3:
        first = a[0]
        second = a[1]
        last = a[-1]

        for c in first:
            if c in second and c in last:
                return [c, True]
    
    return [None, False]

sumPriority = 0
for group in fileData:
    commonChar = commonCharacter(group)

    badge = commonChar[0]
    priority = alphabets.index(badge) + 1
    print(priority)

    sumPriority += priority

print("Sum Priority:", sumPriority)
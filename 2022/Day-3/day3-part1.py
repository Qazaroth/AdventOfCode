import string

alphabets = list(string.ascii_lowercase) + list(string.ascii_uppercase)

inputFile = open("input.txt", "r")
inputFileData = inputFile.read().splitlines()
fileData = []

for i in inputFileData:
    length = len(i)
    n = int(length/2)
    chunks = [i[a:a+n] for a in range(0, length, n)]

    c1 = chunks[0]
    c2 = chunks[1]

    for c3 in c1:
        if c3 in alphabets and c3 in c2:
            chunks.append(alphabets.index(c3) + 1)
            break

    fileData.append(chunks)

fileData.sort(key=lambda x : x[-1])
totalPriority = 0
for f in fileData:
    priority = f[-1]
    totalPriority += priority
    
print(totalPriority)
# print(fileData)
f_in = open('input_09.txt', 'r', encoding='utf-8')
dMap = f_in.readline()
f_in.close()
# print(len(dMap))
fMap = []
i = 0
f = 0
while i < len(dMap):
    for j in range(int(dMap[i])):
        fMap.append(f)
    f += 1
    if i + 1 < len(dMap):
        for j in range(int(dMap[i+1])):
            fMap.append(-1)
    i += 2
# print(*fMap)
j = len(fMap) - 1
for i in range(len(fMap)):
    if fMap[i] == -1:
        #swap from the end
        while fMap[j] == -1 and j > i:
            j -= 1
        if j > i:
            fMap[i], fMap[j] = fMap[j], fMap[i]
    i += 1
# print(*fMap)
# j-1 - last block of last file
checkSum = sum(i*fMap[i] for i in range(j))
print(checkSum)
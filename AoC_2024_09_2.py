from time import time
class dChunk:
    def __init__(self, f: int, l: int):
        self.first_block = f
        self.length = l


class dFile(dChunk):
    def __init__(self, i:int, f: int, l: int):
        self.id = i
        dChunk.__init__(self, f, l)

    def checkS(self):
        return self.id * sum(self.first_block + j for j in range(self.length))


def moveFile(f:int, fr:int):
    # File could be transferred forward only, so no need to reclaim freed space
    if fileMap[f].length < freeMap[fr].length:
        fileMap[f].first_block = freeMap[fr].first_block
        freeMap[fr].first_block += fileMap[f].length
        freeMap[fr].length -= fileMap[f].length
    elif fileMap[f].length == freeMap[fr].length:
        fileMap[f].first_block = freeMap[fr].first_block
        freeMap.remove(freeMap[fr])


start_time = time()
f_in = open('input_09.txt', 'r', encoding='utf-8')
dMap = f_in.readline()
f_in.close()
fileMap = []
freeMap = []
i = 0
f = -1
curB = 0
while i < len(dMap):
    curL = int(dMap[i])
    f += 1
    nFile = dFile(f, curB, curL)
    curB += curL
    fileMap.append(nFile)
    if i + 1 < len(dMap):
        curL = int(dMap[i+1])
        if curL > 0:
            nFree = dChunk(curB, curL)
            curB += curL
            freeMap.append(nFree)
    i += 2
f = len(fileMap) - 1
while f >= 0:
    fr = 0
    while fr < len(freeMap) and fileMap[f].first_block > freeMap[fr].first_block and fileMap[f].length > freeMap[fr].length:
        fr += 1
    if fr < len(freeMap) and fileMap[f].first_block > freeMap[fr].first_block and fileMap[f].length <= freeMap[fr].length:
        moveFile(f, fr)
    f -= 1
checkSum = sum(f.checkS() for f in fileMap)
print(checkSum)
print("--- %s seconds ---" % round(time() - start_time, 3))

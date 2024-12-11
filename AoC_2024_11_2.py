from time import time
import math
def nextG(src: dict) -> dict:
    res = {}
    for k in src.keys():
        if k == 0:
            res[1] = res.get(1, 0) + src[k]
        else:
            m = int(math.log10(k)) + 1
            if m % 2 == 0:
                pw = math.pow(10, round(m/2))
                r = k % pw
                l = round((k - r) / pw)
                res[r] = res.get(r, 0) + src[k]
                res[l] = res.get(l, 0) + src[k]
            else:
                r = k * 2024
                res[r] = res.get(r, 0) + src[k]
    return res

t = time()
for c in open('input_11.txt', 'r', encoding='utf-8'):
    sDict = {}
    stones = list(map(int, c.strip().split()))
    for s in stones:
        sDict[s] = sDict.get(s, 0) + 1
for j in range(75):
    sDict = nextG(sDict)
print("total keys: %6d" % len(sDict.keys()))
s = sum(sDict[k] for k in sDict.keys())
print("Total stones", s)
print("Total time: %s seconds" % round(time() - t, 3))

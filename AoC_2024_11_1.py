from time import time
import math
def nextG(src: list) -> list:
    res = []
    for e in src:
        if e == 0:
            res.append(1)
        else:
            m = int(math.log10(e)) + 1
            if m % 2 == 0:
                p = math.pow(10, round(m/2))
                r = e % p
                res.append(round((e - r) / p))
                res.append(r)
            else:
                res.append(e * 2024)
    return res

t = time()
for c in open('input_11.txt', 'r', encoding='utf-8'):
    stones = list(map(int, c.strip().split()))
print(*stones)
for j in range(25):
    t1 = time()
    stones = nextG(stones)
    print("Iteration: %2d. Elapsed %s seconds" % (j + 1, round(time() - t1, 3)))
print(len(stones))
print("Total %s seconds" % round(time() - t, 3))

from time import time
import math
def nextG():
    N = len(stones)
    for i in range(N):
        if stones[i] == 0:
            stones[i] = 1
        else:
            m = int(math.log10(stones[i])) + 1
            if m % 2 == 0:
                p = math.pow(10, round(m/2))
                r = stones[i] % p
                stones[i] = round((stones[i] - r) / p)
                stones.append(r)
            else:
                stones[i] *= 2024


t = time()
for c in open('input_11.txt', 'r', encoding='utf-8'):
    stones = list(map(int, c.strip().split()))
print(*stones)
for j in range(75):
    t1 = time()
    nextG()
    print("Iteration: %2d. Elapsed %s seconds" % (j + 1, round(time() - t1, 3)))
print(len(stones))
print("Total %s seconds" % round(time() - t, 3))

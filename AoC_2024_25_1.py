from itertools import product
from operator import add
locks = []
keys = []
data = open('input_25.txt', 'r', encoding='utf-8').read().split('\n\n')
for i, block in enumerate(data):
    lines = block.splitlines()
    cnt = [0, 0, 0, 0, 0]
    for j in range(1, 6):
        for p in range(5):
            cnt[p] += lines[j][p] == '#'
    if lines[0] == '.....':
        keys.append(cnt)
    else:
        locks.append(cnt)
fits = 0
for l, k in product(locks, keys):
    fits += max([a + b for a, b in zip(l, k)]) <= 5
print('Part 1 answer: ', fits)
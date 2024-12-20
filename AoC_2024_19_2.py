from time import time
from functools import cache

@cache
def how_many(des):
    res = 0
    if not des:
        return 0
    for t in towels:
        if t == des:
            res += 1
        elif len(t) < len(des) and t == des[:len(t)]:
            res += how_many(des[len(t):])
    return res

start_time = time()
designs = []
for i, ln in enumerate(open('input_19.txt', 'r', encoding='utf-8')):
    lin = ln.strip()
    if i == 0:
        towels = list(lin.split(', '))
    else:
        if lin:
            designs.append(lin)
s = 0
cnt = 0
for d in designs:
    s += how_many(d)
print("Part 2 answer:", s)
print(how_many.cache_info())
print("Elapsed time: %s seconds" % round(time() - start_time, 3))

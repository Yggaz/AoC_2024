from time import time

start_time = time()
eff_limit = 100
cheat_limit = 20
walls = set()
path = []
data = open('input_20.txt', 'r', encoding='utf-8').read()
for x, line in enumerate(data.split()):
    for y, c in enumerate(line.strip()):
        match c:
            case '#': walls.add((x, y))
            case 'S': source = (x, y)
            case 'E': target = (x,y)
N = x + 1
path.append(source)
cur = source
while cur != target:
    x, y = cur
    if (x - 1, y) not in walls and (x - 1, y) not in path:
        cur = (x - 1, y)
    elif (x + 1, y) not in walls and (x + 1, y) not in path:
        cur = (x + 1, y)
    elif (x, y - 1) not in walls and (x, y - 1) not in path:
        cur = (x, y - 1)
    elif (x, y + 1) not in walls and (x, y + 1) not in path:
        cur = (x, y + 1)
    else:
        break
    path.append(cur)
base_cost = len(path) - 1
print('Сost with all walls', base_cost)
effective = 0
best = 0
xfrom, yfrom = source
xto, yto = source
for c, step in enumerate(path):
    if len(path) - c < eff_limit:
        break
    if c > 0 and c % 100 == 0:
        print('Processed nodes:', c)
    x, y = step
    for k in [(xx, yy) for (xx, yy) in path if 0 < abs(xx-x)+abs(yy-y) <= cheat_limit]:
        xb, yb = k
        short = path.index(k) - (abs(xb - x)+abs(yb - y)) - c
        if short >= eff_limit:
            effective += 1
            if short > best:
                best = short
                xfrom, xfrom = step
                xto, yto = k
print("Part 2 answer:", effective)
print('Best shortcut: from (%d,%d) to (%d,%d). Cost: %d, effect: %d' % (xfrom, yfrom, xto, yto,abs(xfrom - xto)+abs(yfrom - yto) ,best))
print("Elapsed time: %s seconds" % round(time() - start_time, 3))

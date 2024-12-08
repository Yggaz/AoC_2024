def antPos():
    res = {}
    global N
    for i, ln in enumerate(open('input_08.txt', 'r', encoding='utf-8')):
        if N == 0:
            N = len(ln) - 1
        for j in range(N):
            if  ln[j] != '.':
                if res.get(ln[j], 0) == 0:
                    res[ln[j]] = list()
                res[ln[j]].append(tuple((i, j)))
                #print(ln[j], i, j)
    return res

def antinode(a1, a2):
    global N
    dx = a1[0] - a2[0] # a2x + dx = a1x
    dy = a1[1] - a2[1] # a2y + dy = a1y
    t1x = a1[0] + dx
    t1y = a1[1] + dy
    t2x = a2[0] - dx
    t2y = a2[1] - dy
    if 0 <= t1x < N and 0 <= t1y < N:
        aNodes.add(tuple((t1x, t1y)))
    if 0 <= t2x < N and 0 <= t2y < N:
        aNodes.add(tuple((t2x, t2y)))

def antinode2(a1, a2):
    global N
    aNodes2.add(tuple((a1[0], a1[1])))
    aNodes2.add(tuple((a2[0], a2[1])))
    dx = a1[0] - a2[0] # a2x + dx = a1x
    dy = a1[1] - a2[1] # a2y + dy = a1y
    t1x = a1[0] + dx
    t1y = a1[1] + dy
    t2x = a2[0] - dx
    t2y = a2[1] - dy
    while 0 <= t1x < N and 0 <= t1y < N:
        aNodes2.add(tuple((t1x, t1y)))
        t1x += dx
        t1y += dy
    while 0 <= t2x < N and 0 <= t2y < N:
        aNodes2.add(tuple((t2x, t2y)))
        t2x -= dx
        t2y -= dy


N = 0
ants = antPos()
aNodes = set()
aNodes2 = set()
print(N)
for k in ants.keys():
    l = len(ants[k])
    for i in range(l-1):
        for j in range(i + 1, l):
            antinode(ants[k][i], ants[k][j])
            antinode2(ants[k][i], ants[k][j])
print(len(aNodes))
print(len(aNodes2))

def adjacent(v: int, cur: dict) -> dict:
    global N
    res = {}
    vv = str(v + 1)
    for t in cur.keys():
        x = t[0]
        y = t[1]
        r = cur.get(t, 0)
        dx1 = x - 1 if x > 0 else x
        dx2 = x + 1 if x < N - 1 else x
        dy1 = y - 1 if y > 0 else y
        dy2 = y + 1 if y < N - 1 else y
        if tMap[x][dy1] == vv:
            tt = tuple((x, dy1))
            res[tt] = res.get(tt, 0) + r
        if tMap[x][dy2] == vv:
            tt = tuple((x, dy2))
            res[tt] = res.get(tt, 0) + r
        if tMap[dx1][y] == vv:
            tt = tuple((dx1, y))
            res[tt] = res.get(tt, 0) + r
        if tMap[dx2][y] == vv:
            tt = tuple((dx2, y))
            res[tt] = res.get(tt, 0) + r
    return res

heads = {}
tMap = []
for i, ln in enumerate(open('input_10.txt', 'r', encoding='utf-8')):
    tMap.append(ln.strip())
    for j, c in enumerate(ln):
        if ln[j] == "0":
            heads[tuple((i,j))] = 0
N = len(tMap)
s = 0
s1 = 0
for k in heads.keys():
    curP = {}
    curP[k] = 1
    for curV in range(9):
        curP = adjacent(curV, curP)
    for kk in curP.keys():
        s1 += curP[kk]
    heads[k] = len(curP)
    s += len(curP)
print(s)
print(s1)

def adjacent(v: int, cur: set) -> set:
    global N
    res = set()
    vv = str(v + 1)
    for t in cur:
        dx1 = t[0] - 1 if t[0] > 0 else t[0]
        dx2 = t[0] + 1 if t[0] < N - 1 else t[0]
        dy1 = t[1] - 1 if t[1] > 0 else t[1]
        dy2 = t[1] + 1 if t[1] < N - 1 else t[1]
        if tMap[t[0]][dy1] == vv:
            res.add(tuple((t[0],dy1)))
        if tMap[t[0]][dy2] == vv:
            res.add(tuple((t[0],dy2)))
        if tMap[dx1][t[1]] == vv:
            res.add(tuple((dx1,t[1])))
        if tMap[dx2][t[1]] == vv:
            res.add(tuple((dx2,t[1])))
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
for k in heads.keys():
    curP = set()
    curP.add(k)
    for curV in range(9):
        curP = adjacent(curV, curP)
    heads[k] = len(curP)
    s += len(curP)
print(s)
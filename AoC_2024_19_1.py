import heapq
designs = []
for i, ln in enumerate(open('input_19.txt', 'r', encoding='utf-8')):
    lin = ln.strip()
    if i == 0:
        towels = list(lin.split(', '))
    else:
        if lin:
            designs.append(lin)
indep = []
for j, d in enumerate(towels):
    solved = False
    q = [(len(d), d)]
    cnt = 0
    while q:
        l, des = heapq.heappop(q)
        for k, t in enumerate(towels):
            if k == j:
                continue
            elif t == des:
                solved = True
                break
            elif t == des[:len(t)]:
                heapq.heappush(q, (len(des[len(t):]), des[len(t):]))
    if not solved:
        indep.append(d)
good = []
bad = []
for j, d in enumerate(designs):
    solved = False
    q = [(len(d), d)]
    cnt = 0
    while q:
        l, des = heapq.heappop(q)
        for t in indep:
            if t == des:
                solved = True
                break
            elif t == des[:len(t)]:
                heapq.heappush(q, (len(des[len(t):]), des[len(t):]))
        cnt += 1
    if solved:
        good.append(j)
    else:
        bad.append(j)
print(len(good))
print(good)
print(len(bad))


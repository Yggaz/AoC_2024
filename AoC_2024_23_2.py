from itertools import combinations
data = open('input_23.txt', 'r', encoding='utf-8').read().splitlines()
connections = set()
computers = set()
lans = []
max_lan = 0
for ln in data:
    fir, sec = ln.split('-')
    computers.add(fir)
    computers.add(sec)
    connections.add((fir, sec))
    connections.add((sec, fir))
for c in computers:
    connected = set((x for x in computers if (c, x) in connections))
    cur = len(connected)
    go_on = cur > max_lan
    while go_on:
        for tryout in combinations(connected, cur):
            tmp_lan = set()
            if all((p[0], p[1]) in connections for p in combinations(tryout, 2)):
                max_lan = cur
                go_on = False
                tmp_lan.add(c)
                tmp_lan = tmp_lan.union(set(tryout))
                if tmp_lan not in lans:
                    if len(lans) > 0 and max(len(l) for l in lans) < len(tmp_lan):
                        lans = []
                    lans.append(tmp_lan)
        if go_on:
            cur -= 1
            if cur <= max_lan:
                go_on = False
for lan in lans:
    print('Answer for part 2: ', end='')
    print(*sorted(list(lan)), sep=',')


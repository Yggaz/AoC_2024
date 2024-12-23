from itertools import combinations
from operator import countOf

data = open('input_23.txt', 'r', encoding='utf-8').read().splitlines()
connections = set()
computers = set()
lans = []
for ln in data:
    fir, sec = ln.split('-')
    computers.add(fir)
    computers.add(sec)
    connections.add((fir, sec))
    connections.add((sec, fir))
print('Computers: ', *computers)
print('Connections: ', *connections)
max_lan = 0
for c in computers:
    connected = set((x for x in computers if (x, c) in connections))
    cur = len(connected)
    go_on = cur > max_lan
    while go_on:
        tmp_lan = set()
        for tryout in combinations(connected, cur):
            if all((p[0], p[1]) in connections for p in combinations(tryout, 2)):
                max_lan = len(tryout)
                go_on = False
                tmp_lan.add(c)
                for cc in tryout:
                    tmp_lan.add(cc)
                if tmp_lan not in lans:
                    lans.append(tmp_lan)
        if go_on:
            cur -= 1
            if cur < max_lan:
                go_on = False
for lan in lans:
    if any((p[0], p[1]) not in connections for p in combinations(lan, 2)):
        pass
    else:
        print(*sorted(list(lan)), sep=',')

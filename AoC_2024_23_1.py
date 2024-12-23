from itertools import combinations
data = open('input_23.txt', 'r', encoding='utf-8').read().splitlines()
connections = dict()
computers = []
three = []
for ln in data:
    fir, sec = ln.split('-')
    if sec not in connections.get(fir,[]):
        if len(connections.get(fir,[])) == 0:
            connections[fir] = [sec]
        else:
            connections[fir].append(sec)
    if fir not in connections.get(sec,[]):
        if len(connections.get(sec,[])) == 0:
            connections[sec] = [fir]
        else:
            connections[sec].append(fir)
for k in connections.keys():
    if k[0] == 't':
        for comps in combinations(connections[k], 2):
            if comps[0] in connections[comps[1]]:
                tmp = sorted([k, comps[0], comps[1]])
                if tmp not in three:
                    three.append(tmp)
print('Answer for part 1:', len(three))

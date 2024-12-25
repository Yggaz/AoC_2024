locks = []
keys = []
data = open('input_25.txt', 'r', encoding='utf-8').read().split('\n\n')
for i, block in enumerate(data):
    lines = block.splitlines()
    cnt = [0, 0, 0, 0, 0]
    for j in range(1, 6):
        for p in range(5):
            cnt[p] += 1 if lines[j][p] == '#' else 0
    if lines[0] == '.....':
        keys.append(cnt)
    else:
        locks.append(cnt)
fits = 0
for l in locks:
    for k in keys:
        tmp = [sum(x) for x in zip(l, k)]
        if max(tmp) <= 5:
            fits += 1
print('Part 1 answer: ', fits)
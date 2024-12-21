# 208126 is too high
# 205950 is not right
# 202870 is too low
numpad = {
    '7': [('8', '>'), ('4', 'v')],
    '8': [('7', '<'), ('5', 'v'), ('9', '>')],
    '9': [('8', '<'), ('6', 'v')],
    '4': [('7', '^'), ('5', '>'), ('1', 'v')],
    '5': [('8', '^'), ('4', '<'), ('2', 'v'), ('6', '>')],
    '6': [('9', '^'), ('5', '<'), ('3', 'v')],
    '1': [('4', '^'), ('2', '>')],
    '2': [('1', '<'), ('5', '^'), ('3', '>'), ('0', 'v')],
    '3': [('A', 'v'), ('2', '<'), ('6', '^')],
    '0': [('2', '^'), ('A', '>')],
    'A': [('0', '<'), ('3', '^')]
}

direct = {
    '^': [('A', '>'), ('v', 'v')],
    'A': [('^', '<'), ('>', 'v')],
    '<': [('v', '>')],
    'v': [('<', '<'), ('^', '^'), ('>', '>')],
    '>': [('v', '<'), ('A', '^')],
}


def find_paths(start, stop, pad):
    q = [(start, '')]
    done = {start}
    shortest = None
    res = []
    while q:
        cur, path = q.pop(0)
        done.add(cur)
        if cur == stop:
            if shortest is None:
                shortest = len(path)
            if len(path) == shortest:
                res.append(path + 'A')
            continue
        if shortest and len(path) >= shortest:
            continue
        for nei, d in pad[cur]:
            done.add(nei)
            q.append((nei, path + d))
    return res

def decode(cod, level, cpad):
    res = 0
    cod = "A" + cod
    for i in range(len(cod) - 1):
        start, stop = cod[i], cod[i + 1]
        paths = find_paths(start, stop, cpad)
        if level == 0:
            res += min(map(len, paths))
        else:
            res += min(decode(path, level - 1, direct) for path in paths)
    return res

data = open('input_21.txt', 'r', encoding='utf-8').read()
answer1 = 0
for i, code in enumerate(data.split()):
    print(code)
    l1 = decode(code, 2, numpad)
    part1 = int(code[:-1])
    print('%d * %d = %d' % (l1, part1, l1 * part1))
    answer1 += l1 * part1
print('Part 1 answer:', answer1)


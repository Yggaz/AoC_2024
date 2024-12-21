# 208126 is too high
# 205950 is not right
# 202870 is too low
from functools import cache
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
    shortest = 100 # will be enough
    res = []
    while q:
        # take from the beginning
        cur, path = q.pop(0)
        if cur == stop:
            if shortest > len(path):
                # new best length
                shortest = len(path)
                res = []
            if len(path) == shortest:
                # add current path
                res.append(path + 'A')
            continue
        if len(path) >= shortest:
            continue
        for neighbour, step in pad[cur]:
            # add to the end
            q.append((neighbour, path + step))
    return res

@cache
def decode(code, level, pad_name):
    if pad_name == 'numpad':
        pad = numpad
    elif pad_name == 'direct':
        pad = direct
    res = 0
    code = 'A' + code
    for i in range(len(code) - 1):
        start, stop = code[i], code[i + 1]
        paths = find_paths(start, stop, pad)
        if level == 0:
            res += min(map(len, paths))
        else:
            res += min(decode(path, level - 1, 'direct') for path in paths)
    return res

data = open('input_21.txt', 'r', encoding='utf-8').read()
answer1 = 0
answer2 = 0
for i, code in enumerate(data.split()):
    print(code)
    l1 = decode(code, 2, 'numpad')
    l2 = decode(code, 25, 'numpad')
    part1 = int(code[:-1])
    print('%d * %d = %d' % (l1, part1, l1 * part1))
    answer1 += l1 * part1
    print('%d * %d = %d' % (l2, part1, l2 * part1))
    answer2 += l2 * part1
print('Part 1 answer:', answer1)
print('Part 2 answer:', answer2)
print(decode.cache_info())

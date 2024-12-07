def check(t: tuple) -> bool:
    res = True
    for i in range(len(t) - 1):
        res = res and check_two(t[i], t[i + 1])
    return res

def check_two(fir: int, sec:int) -> bool:
    res = sec in rules and fir in rules.get(sec)
    return res


def get_middle(t: tuple) -> int:
    return t[round((len(t) - 1) / 2)]


def correct_one(t: tuple) -> tuple:
    res = []
    i = 0
    while len(res) < len(t):
        if i < len(t) - 1 and not check_two(t[i], t[i + 1]):
            res.append(t[i + 1])
            res.append(t[i])
            i += 2
        else:
            res.append(t[i])
            i += 1
    return tuple(res)


f_in = open('input_05.txt', 'r', encoding='utf-8')
# rules is a dictionary. Key is the FOLLOWING item, value is a list of
# possible preceding items. 21|97 adds 21 to the list of possible preceding values for 97
rules = {}
reps = []
for ln in f_in:
    rule = ln.split('|')
    if len(rule) == 2:
        if not rules.get(int(rule[1])):
            rules[int(rule[1])] = []
        rules[int(rule[1])].append(int(rule[0]))
    else:
        rep = ln.split(',')
        if len(rep) > 1:
            reps.append(tuple(map(int, rep)))
f_in.close()
s = 0
ss = 0
for r in reps:
    if check(r):
        s += get_middle(r)
    else:
        while not check(r):
            r = correct_one(r)
        ss += get_middle(r)
print(s)
print(ss)

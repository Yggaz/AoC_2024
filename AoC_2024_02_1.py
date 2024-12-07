import copy
def check(ll):
    d = ll[1] - ll[0]
    safe = (d != 0)
    for i, cur in enumerate(ll):
        if i > 0:
            safe = (safe and
                    ((cur - ll[i-1]) * d > 0) and
                    (abs(cur - ll[i-1]) <= 3)
                    )
    return safe


f_in = open('input_02.txt', 'r', encoding='utf-8')
safes = 0
for c in f_in:
    l = list(map(int, c.strip().split()))
    if check(l):
        safes += 1
print (safes)
f_in.close()

f_in = open('input_02.txt', 'r', encoding='utf-8')
safes = 0
for c in f_in:
    l = list(map(int, c.strip().split()))
    safe = check(l)
    if not safe:
        i = 0
        zer = 0
        pos = 0
        neg = 0
        last_p = 0
        last_n = 0
        last_z = 0
        while i < len(l) - 1:
            i += 1
            if l[i] == l[i-1]:
                zer += 1
                last_z = i
            if l[i] > l[i-1]:
                pos += 1
                last_p = i
            if l[i] < l[i-1]:
                neg += 1
                last_n = i
        # more than 1 equal or both pos and neg greater than one
        if (zer > 1) or ((pos + zer > 1) and (neg + zer > 1)):
            safe = False
        else:
            if zer == 1:
                del l[last_z]
                safe = check(l)
            elif neg == 1:
                l2 = copy.copy(l)
                del l[last_n]
                del l2[last_n - 1]
                safe = check(l) or check(l2)
            elif pos == 1:
                l2 = copy.copy(l)
                del l[last_p]
                del l2[last_p - 1]
                safe = check(l) or check(l2)
            else:
                l2 = copy.copy(l)
                del l[0]
                del l2[len(l2) - 1]
                safe = check(l) or check(l2)
    if safe:
        safes += 1
print (safes)

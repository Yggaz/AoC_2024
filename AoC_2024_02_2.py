f_in = open('input_02.txt', 'r', encoding='utf-8')
safes = 0
not_good = 0
too_much = 0
ln = 0
for c in f_in:
    ln += 1
    l = list(map(int, c.strip().split()))
    i = 0
    pos = 0
    neg = 0
    zer = 0
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
        not_good += 1
        d = 0
    else:
        safe = True
        used = False
        if zer == 1:
            del l[last_z]
            used = True
        if neg == 1:
            # Many pos, one neg.
            # current < previous
            if last_n < len(l) - 1:
                # next one exists
                if l[last_n + 1] <= l[last_n - 1]:
                    # next exists and not greater than previous - the only chance is to drop previous
                    last_n -= 1
            else:
                # no next one
                if l[last_n] > l[last_n - 2]:
                    last_n -= 1
            del l[last_n]
            used = True
        if pos == 1:
            # Many neg, one pos.
            # current > previous
            d = -1
            if last_p < len(l) - 1:
                # next one exists
                if l[last_p + 1] >= l[last_p - 1]:
                    # next exists and not less than previous - the only chance is to drop previous
                    last_p -= 1
            else:
                # no next one
                if l[last_p] < l[last_p - 2]:
                    last_p -= 1
            del l[last_p]
            used = True
        if not used and abs (l[0] - l[1]) > 3:
            used = True
            del l[0]
        if not used and abs (l[len(l) - 1] - l[len(l) - 2] ) > 3:
            used = True
            del l[len(l) - 1]
        if pos > neg:
            d = 1
        else:
            d = -1
        for i, cur in enumerate(l):
            if i > 0:
                if safe and cur == l[i-1]:
                    safe = False
                if safe and (cur - l[i-1]) * d < 0:
                    safe = False
                if safe and abs(cur - l[i-1]) > 3:
                    safe = False
        if not safe:
            too_much += 1
    if safe:
        safes += 1
print ("Too much bad levels:", not_good)
print ("Wrong slope:", too_much)
print (safes)

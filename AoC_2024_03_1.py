def mul(s):
    res = 0
    if s and (s[0] == "("):
        i = s.find(")")
        if i > 0:
            ss = s[1:i].split(",")
            if len(ss) == 2:
                if ss[0].isdigit() and ss[1].isdigit():
                    res = int(ss[0]) * int(ss[1])
    return res

f_in = open('input_03.txt', 'r', encoding='utf-8')
res = 0
i = 0
for c in f_in:
    res += sum(map(mul, ('mul[' + c).split('mul')))
print (res)
f_in.close()

f_in = open('input_03.txt', 'r', encoding='utf-8')
res = 0
p = 0
for c in f_in:
    if p >= 0:
        c = 'do()' + c
    for line in c.split("don't()"):
        p = line.find('do()')
        if p >= 0:
            res += sum(map(mul, (line[p:]).split('mul')))
print (res)
f_in.close()


class Rule:
    def __init__(self, gin1, gin2, goper, gout):
        self.in1 = gin1
        self.in2 = gin2
        self.oper = goper
        self.out = gout

    def ready(self) -> bool:
        return (self.in1 in memory.keys()) and (self.in2 in memory.keys())

    def __str__(self):
        return self.in1 + ' ' + self.oper + ' ' + self.in2 + ' -> ' + self.out

    def produce(self):
        if self.ready():
            match self.oper:
                case 'AND':
                    memory[self.out] = memory[self.in1] & memory[self.in2]
                case 'OR':
                    memory[self.out] = memory[self.in1] | memory[self.in2]
                case 'XOR':
                    memory[self.out] = memory[self.in1] ^ memory[self.in2]

def test_run(xx, yy):
    memory.clear()
    x = xx
    y = yy
    xbin = bin(x)[2:].zfill(45)
    ybin = bin(y)[2:].zfill(45)
    for i in range(45):
        j = 44 - i
        kx = 'x' + str(j).zfill(2)
        ky = 'y' + str(j).zfill(2)
        memory[kx] = int(xbin[i])
        memory[ky] = int(ybin[i])
    run()

def run():
    # running
    done = False
    cnt = 0
    while not done:
        done = True
        cnt += 1
        for r in rules:
            if not r.ready():
                done = False
            else:
                r.produce()
        if cnt > 100:
            done = True

def check(show = True) -> bool:
    z = ''
    x = ''
    y = ''
    # x, y - 45 bits (00 - 44), z - 46 bits (00-45)
    for m in sorted(memory.keys()):
        match m[0]:
            case 'z':
                z = str(memory[m]) + z
            case 'x':
                x = str(memory[m]) + x
            case 'y':
                y = str(memory[m]) + y
    corr = bin(int(x, 2) + int(y, 2))[2:].zfill(46)
    if show and z != corr:
        print('x:  ', x)
        print('y:  ', y)
        print('z: ', z)
        print('c: ', corr)
    return z == corr

def swap(f,t):
    ff, tt = 00, 00
    for i, r in enumerate(rules):
        if r.out == f:
            ff = i
        elif r.out == t:
            tt = i
    rules[ff].out = t
    rules[tt].out = f


def prn(out, lng=1):
    for rr in (r for r in rules if r.out == out):
        if rr.in1[0] == 'x':
            res_1 = rr.in1
        else:
            res_1 = '( '+ prn(rr.in1, 0) + ')'
        if rr.in2[0] == 'y':
            res_2 = rr.in2
        else:
            res_2 = '( '+ prn(rr.in2, 0) + ')'
        if lng == 1:
            res = rr.out + ' <- ' + res_1 + ' ' + rr.oper + ' ' + res_2
        else:
            res = rr.out +' '+ res_1 + ' ' + rr.oper + ' ' + res_2
        return res



data = open('input_24.txt', 'r', encoding='utf-8').read().splitlines()
program_mode = False
input_mode = False
memory = dict()
gates = set()
rules = []
for ln in data:
    if len(ln) == 0:
        program_mode = True
    elif program_mode:
        r = ln.split(' -> ')
        ops = r[0].split(' ')
        rule = Rule(ops[0], ops[2], ops[1], r[1])
        rules.append(rule)
        gates.add(r[1])
    else:
        if input_mode:
            ops = ln.split(': ')
            memory[ops[0]] = int(ops[1])

print(prn('z00'))
print(prn('z01'))
print(prn('z02'))
print(prn('z03'))
print(prn('z04'))
print(prn('z05'))
print(prn('z06'))
print(prn('z07'))
print(prn('z08'))
print(prn('z09'))

print(prn('z10'))
print(prn('z11'))
print(prn('z12'))
print(prn('z13'))
print(prn('z14'))
print(prn('z15'))
print(prn('z16'))
print(prn('z17'))
print(prn('z18'))
print(prn('z19'))

print(prn('z20'))
print(prn('z21'))
print(prn('z22'))
print(prn('z23'))
print(prn('z24'))
print(prn('z25'))
print(prn('z26'))
print(prn('z27'))
print(prn('z28'))
print(prn('z29'))

print(prn('z30'))
print(prn('z31'))
print(prn('z32'))
print(prn('z33'))
print(prn('z34'))
print(prn('z35'))
print(prn('z36'))
print(prn('z37'))
print(prn('z38'))
print(prn('z39'))

print(prn('z40'))
print(prn('z41'))
print(prn('z42'))
print(prn('z43'))
print(prn('z44'))
print(prn('z45'))

swap('z05', 'frn')
swap('z21', 'gmq')
swap('vtj', 'wnf')
swap('z39', 'wtt')

good = True

x = 2**38 - 1
y = 2**44 - 1
test_run(x, y)
good = check()


if good:
    print('Great!')
else:
    print('not good!')

answer2 = ['frn','z05','gmq','z21','vtj','wnf','z39','wtt']
print(*sorted(answer2), sep=',')

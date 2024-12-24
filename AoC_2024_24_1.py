class Rule:
    def __init__(self, gin1, gin2, goper, gout):
        self.in1 = gin1
        self.in2 = gin2
        self.oper = goper
        self.out = gout

    def ready(self) -> bool:
        return (self.in1 in memory.keys()) and (self.in2 in memory.keys())

    def produce(self):
        if self.ready():
            match self.oper:
                case 'AND':
                    memory[self.out] = memory[self.in1] & memory[self.in2]
                case 'OR':
                    memory[self.out] = memory[self.in1] | memory[self.in2]
                case 'XOR':
                    memory[self.out] = memory[self.in1] ^ memory[self.in2]


data = open('input_24.txt', 'r', encoding='utf-8').read().splitlines()
input_mode = True
memory = dict()
rules = []
for ln in data:
    if len(ln) == 0:
        input_mode = False
    elif input_mode:
        ops = ln.split(': ')
        memory[ops[0]] = int(ops[1])
    else:
        r = ln.split(' -> ')
        ops = r[0].split(' ')
        rule = Rule(ops[0], ops[2], ops[1], r[1])
        rules.append(rule)
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
    if cnt > 1000:
        done = True
print('Done!')
res = ''
for m in sorted(memory.keys()):
    if m[0] == 'z':
        res = str(memory[m]) + res
answer1 = int(res, 2)
print('Answer for part 1:', answer1)

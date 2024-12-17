reg = {"A": 0, "B": 0, "C":0}
prg = []
out_line = ""

def combo(cop):
    if cop == 4:
        return reg["A"]
    elif cop == 5:
        return reg["B"]
    elif cop == 6:
        return reg["C"]
    else:
        return cop


def adv(cop):
    cop = combo(cop)
    num = reg["A"]
    den = pow(2, cop)
    reg["A"] = num // den
    # print("adv", cop)

def bxl(lop):
    reg["B"] = reg["B"] ^ lop
    # print("bxl", lop)

def bst(cop):
    cop = combo(cop)
    reg["B"] = cop % 8
    # print("bst", cop)

def jnz(lop):
    global pnt
    # print("jnz", lop)
    if reg["A"] != 0:
        pnt = lop - 1

def bxc(iop):
    reg["B"] = reg["B"] ^ reg["C"]
    # print("bxc", iop)

def out(cop):
    global out_line
    cop = combo(cop)
    out_line += "," + str(cop % 8)
    # print("out", cop)

def bdv(cop):
    cop = combo(cop)
    num = reg["A"]
    den = pow(2, cop)
    reg["B"] = num // den
    # print("bdv", cop)

def cdv(cop):
    cop = combo(cop)
    num = reg["A"]
    den = pow(2, cop)
    reg["C"] = num // den
    # print("cdv", cop)

opcode = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


for i, ln in enumerate(open('input_17.txt', 'r', encoding='utf-8')):
    lin = ln.split(":")
    if len(lin) > 1:
        rg = lin[0].split()
        if rg and rg[0] == "Register":
            reg[rg[1]] = int(lin[1])
        else:
            txt = ',' + lin[1].strip()
            for j, c in enumerate(list(map(int, lin[1].split(",")))):
                if j % 2 == 0:
                    op = c
                else:
                    prg.append((op, c))
print(reg)
print(prg)
print(txt[1:])
pnt = 0
while pnt < len(prg):
    opcode[prg[pnt][0]](prg[pnt][1])
    pnt += 1
print(out_line[1:])

reg["A"] = 202356708354602
reg["B"] = 0
reg["C"] = 0
out_line = ""
print(reg)
pnt = 0
while pnt < len(prg):
    opcode[prg[pnt][0]](prg[pnt][1])
    pnt += 1
print(out_line[1:])

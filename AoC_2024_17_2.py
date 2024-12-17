def prg():
    global a, b, c, out
    while True:
        # bst, regA	    : regA mod 8 -> regB		: 3 least bits of A -> B
        # bxl, 1		: regB XOR 1 -> regB		: 0 <-> 1, 2 <-> 3, 4 <-> 5, 6 <-> 7
        b = (a % 8) ^ 1
        # cdv, regB	    : regA // 2**regB -> regC	: A shifted right regB bits -> regC
        c = a // pow(2, b)
        # adv, 3		: regA // 8 -> regA			: A shifts right 3 bits
        a = a // 8
        # bxl, 4	    : regB XOR 4 -> regB
        # bxc			: regB XOR regC -> regB
        b = (b ^ 4) ^ c
        # out, regB	    : out RegB mod 8
        out += str(b % 8)
        # jnz, 0		: if regA <> 0, go from the beginning
        if a == 0:
            break

str2 = ''
str1 = '010101000101010'
str3 = '101011010111'
str4 = '101110000000'
txt = "2411750314405530"

for i in range(511):
    str2 = bin(i)[2:]
    aa = int(str4+str3+str2+str1, 2)
    a = aa
    b = 0
    c = 0
    out = ""
    b = 0
    c = 0
    prg()
    if out == txt:
        print(i, str2)
        print(aa, out)

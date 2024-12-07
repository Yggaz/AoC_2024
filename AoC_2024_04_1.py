f_in = open('input_04.txt', 'r', encoding='utf-8')
text = f_in.readlines()
f_in.close()
N = len(text)
xmas = 0
for line in text:
    xmas += line.count('XMAS') + line.count('SAMX')
for i in range(N):
    t1 = ''
    for j in range(N):
        t1 += text[j][i]
    xmas += t1.count('XMAS') + t1.count('SAMX')
for i in range(N):
    t1 = ''
    t2 = ''
    t3 = ''
    t4 = ''
    for j in range(i):
        # Diagonally \ from top:
        t1 += text[j][N - i + j]
        # Diagonally \ from bottom:
        t2 += text[N - i + j][j]
        # Diagonally / from top:
        t3 += text[i - j - 1][j]
        # Diagonally / from bottom:
        t4 += text[N - j - 1][N - i + j]
    xmas += t1.count('XMAS') + t1.count('SAMX')
    xmas += t2.count('XMAS') + t2.count('SAMX')
    xmas += t3.count('XMAS') + t3.count('SAMX')
    xmas += t4.count('XMAS') + t4.count('SAMX')
t1 = ''
t2 = ''
for j in range(N):
    # Diagonally \
    t1 += text[j][j]
    # Diagonally /
    t2 += text[N - j - 1][j]
xmas += t1.count('XMAS') + t1.count('SAMX')
xmas += t2.count('XMAS') + t2.count('SAMX')
print(xmas)

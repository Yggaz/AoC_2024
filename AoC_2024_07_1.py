from time import time
from itertools import product
def check(num: list, oper: tuple, target: int) -> bool:
    tst = num[0]
    for i, o in enumerate(oper):
        if o == '+':
            tst += num[i+1]
        elif o == '*':
            tst *= num[i+1]
        elif o == '|':
            tst = int(str(tst) + str(num[i + 1]))
    return tst == target

start_time = time()
total = 0
total_2 = 0
tst = 0
for line in open('input_07.txt', 'r', encoding='utf-8'):
    ln = line.split(': ')
    trg = int(ln[0])
    numbers = list(map(int, ln[1].split()))
    oper_set = product('+*', repeat=len(numbers) - 1)
    oper2_set = product('+*|', repeat=len(numbers) - 1)
    fnd = False
    for o in oper_set:
        fnd = check(numbers, o, trg)
        tst += 1
        if fnd:
            break
    total += trg if fnd > 0 else 0
    fnd = False
    for o in oper2_set:
        fnd = check(numbers, o, trg)
        tst += 1
        if fnd:
            break
    total_2 += trg if fnd else 0
print(total)
print(total_2)
print("Checks: ", tst)
print("--- %s seconds ---" % round(time() - start_time, 3))

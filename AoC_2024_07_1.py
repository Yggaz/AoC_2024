from time import time
from itertools import product
def check(num: list, op: tuple, target: int) -> bool:
    tst = num[0]
    for i, s in enumerate(op):
        if s == '+':
            tst += num[i+1]
        elif s == '*':
            tst *= num[i+1]
        elif s == '|':
            tst = int(str(tst) + str(num[i + 1]))
    return tst == target

start_time = time()
total = 0
total_2 = 0
for line in open('input_07.txt', 'r', encoding='utf-8'):
    ln = line.split(': ')
    trg = int(ln[0])
    numbers = list(map(int, ln[1].split()))
    fnd = False
    for o in product('+*', repeat=len(numbers) - 1):
        fnd = check(numbers, o, trg)
        if fnd:
            break
    total += trg if fnd else 0
    fnd = False
    for o in product('+*|', repeat=len(numbers) - 1):
        fnd = check(numbers, o, trg)
        if fnd:
            break
    total_2 += trg if fnd else 0
print(total)
print(total_2)
print("--- %s seconds ---" % round(time() - start_time, 3))

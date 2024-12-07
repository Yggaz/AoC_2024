f_in = open('input_2015_02.txt', 'r', encoding='utf-8')
total = 0
total_r = 0
for line in f_in:
    dims = list(map(int, line.split('x')))
    dims.sort()
    total += 3*dims[0]*dims[1] + 2 *(dims[0] * dims[2] + dims[1] * dims[2])
    total_r += 2 * (dims[0] + dims[1]) + (dims[0]  * dims[1] * dims[2])
f_in.close()
print(total)
print(total_r)

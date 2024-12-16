fish = []
for i in range(9):
    fish.append(0)
for ln in open('input_2021_11.txt', 'r', encoding='utf-8'):
    lin = list(map(int, ln.split(',')))
    for f in lin:
        fish[f] += 1
N = 256
for i in range(N):
    tmp = fish[0]
    for j in range(8):
        fish[j] = fish[j+1]
    fish[8] = tmp
    fish[6] += tmp
    if i == 79:
        s1 = sum(k for k in fish)
        print("Part 1 answer:", s1)
s2 = sum(k for k in fish)
print("Part 2 answer:", s2)

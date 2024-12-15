fish = {}
for i in range(9):
    fish[i] = 0
for ln in open('input_2021_11.txt', 'r', encoding='utf-8'):
    lin = list(map(int, ln.split(',')))
    for f in lin:
        fish[f] = fish.get(f, 0) + 1
# N = 80
N = 256
for i in range(N):
    nxt = {}
    for j in range(8):
        nxt[j] = fish[j+1]
    nxt[6] += fish[0]
    nxt[8] = fish[0]
    fish = nxt
    if i == 79:
        s1 = sum(fish[k] for k in fish.keys())
        print("Part 1 answer:", s1)
s2 = sum(fish[k] for k in fish.keys())
print("Part 2 answer:", s2)

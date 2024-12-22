from time import time
start_time = time()
answer1 = 0
data = open('input_22.txt', 'r', encoding='utf-8').read()
results = dict()
for m, ss in enumerate(list(map(int, data.splitlines()))):
    # 5 last prices for current merchant
    price = []
    # sequences that existed for the current merchant
    seen = set()
    # four initial secret numbers
    for i in range(4):
        s1 = (ss ^ (ss << 6)) & 16777215
        s2 = (s1 ^ (s1 >> 5)) & 16777215
        ss = (s2 ^ (s2 << 11)) & 16777215
        price.append(ss % 10)
    # from now on we can track changes
    for i in range (4, 2000):
        s1 = (ss ^ (ss << 6)) & 16777215
        s2 = (s1 ^ (s1 >> 5)) & 16777215
        ss = (s2 ^ (s2 << 11)) & 16777215
        price.append(ss % 10) # price[4] is the last
        chg = (price[1] - price[0], price[2] - price[1], price[3] - price[2], price[4] - price[3])
        price.pop(0) # price[3] is the last
        if chg not in seen:
            # first time current merchant meets this 4-change
            results[chg] = results.get(chg, 0) + price[3]
            seen.add(chg)
    answer1 +=ss
print('Part 1 answer: ', answer1)
answer2 = max(results[k] for k in results.keys())
print('Part 2 answer: ', answer2)
print("Elapsed time: %s seconds" % round(time() - start_time, 3))
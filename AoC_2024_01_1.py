f_in = open('input_01.txt', 'r', encoding='utf-8')
list1 = []
list2 = []
for c in f_in:
    line = list(map(int, c.strip().split()))
    list1.append(line[0])
    list2.append(line[1])
list1.sort()
list2.sort()
dist = 0
sim = 0
for i, e in enumerate(list1):
    dist += abs(list2[i] - e)
    sim += e * list2.count(e)
print ('Part 1 answer:', dist)
print ('Part 2 answer:', sim)

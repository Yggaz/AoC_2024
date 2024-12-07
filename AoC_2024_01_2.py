f_in = open('input_01.txt', 'r', encoding='utf-8')
list1 = []
list2 = []
for c in f_in:
    line = list(map(int, c.strip().split()))
    list1.append(line[0])
    list2.append(line[1])
sim = 0
for i, e in enumerate(list1):
    sim += e * list2.count(e)
print (sim)

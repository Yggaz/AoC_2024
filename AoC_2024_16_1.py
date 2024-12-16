def neighbours(cur):
    res = set()
    t = cur[0]
    d = cur[1]
    d2 = (-cur[1][0], -cur[1][1])
    dr = set(((0, 1), (0, -1), (1, 0), (-1, 0)))
    dr.remove(d)
    dr.remove(d2)
    for dd in dr:
        if (t,dd) not in done:
            res.add((t,dd))
    tst = ((t[0] - d[0], t[1] - d[1]), d)
    if tst in maze.keys() and tst not in done:
        res.add(tst)
    return res

def process_node(node):
    # Строим множество всех соседей, в которые можем из X попасть.
    cst = maze[node]
    for n in neighbours(node):
        # Каждую вершину из этого множества добавляем в множество задетых.
        touched.add(n)
        if node[0] == n[0]:
            cst2 = 1000
        else:
            cst2 = 1
        # Ставим им цену X + цену перехода, если их цена больше.
        if maze[n] > cst + cst2:
            maze[n] = cst + cst2
    # Помечаем X как готовую и выбрасываем её из множества задетых.
    done.add(node)
    if node in touched:
        touched.remove(node)


touched = set()
done = set()
maze = {}
start_state = ((0, 0), (0, 1))
end_state = (0, 0)
for i, ln in enumerate(open('input_16.txt', 'r', encoding='utf-8')):
    lin = ln.strip()
    for j in range(len(lin)):
        if lin[j] == ".":
            maze[((i, j), (-1, 0))] = 140 * 140 * 1000 * 1000
            maze[((i, j), (1, 0))] = 140 * 140 * 1000 * 1000
            maze[((i, j), (0, -1))] = 140 * 140 * 1000 * 1000
            maze[((i, j), (0, 1))] = 140 * 140 * 1000 * 1000
        elif lin[j] == "S":
            maze[((i, j), (-1, 0))] = 140 * 140 * 1000 * 1000
            maze[((i, j), (1, 0))] = 140 * 140 * 1000 * 1000
            maze[((i, j), (0, -1))] = 140 * 140 * 1000 * 1000
            maze[((i, j), (0, 1))] = 0
            start_state = ((i, j), (0, 1))
        elif lin[j] == "E":
            maze[((i, j), (-1, 0))] = 140 * 140 * 1000 * 1000
            maze[((i, j), (1, 0))] = 140 * 140 * 1000 * 1000
            maze[((i, j), (0, -1))] = 140 * 140 * 1000 * 1000
            maze[((i, j), (0, 1))] = 140 * 140 * 1000 * 1000
            end_state = (i, j)
cur_node = start_state
while True:
    process_node(cur_node)
    s_list = sorted(touched, key=lambda x:maze[x])
    if len(s_list) == 0:
        break
    else:
        cur_node = s_list[0]
s_list = sorted([(-1, 0), (1, 0),  (0, -1),  (0, 1)], key=lambda x:maze[(end_state, x)])
last_state = (end_state, s_list[0])
answer_part_1  = maze[last_state]
print(*last_state)
print(answer_part_1)

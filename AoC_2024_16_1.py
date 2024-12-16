from time import time
from copy import deepcopy
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
    s1 = node[0]
    for n in neighbours(node):
        s2 = n[0]
        # Каждую вершину из этого множества добавляем в множество задетых.
        touched.add(n)
        if node[0] == n[0]:
            cst2 = 1000
        else:
            cst2 = 1
        # Ставим им цену X + цену перехода, если их цена больше.
        if maze[n] > cst + cst2:
            maze[n] = cst + cst2
            if cst2 == 1:
                maze_ways[s2] = []
                for way in maze_ways[s1]:
                    tmp = deepcopy(way)
                    tmp.add(s2)
                    maze_ways[s2].append(tmp)
        elif maze[n] == cst + cst2 and cst2 == 1:
            for way in maze_ways[s1]:
                tmp = deepcopy(way)
                tmp.add(s2)
                maze_ways[s2].append(tmp)
        # Magical constant from Part 1 - it won't work without it!
        if maze[n] > 66404: # 66404
            done.add(n)
            touched.remove(n)
    # Помечаем X как готовую и выбрасываем её из множества задетых.
    done.add(node)
    if node in touched:
        touched.remove(node)

def draw_maze(w, h):
    for row in range(h):
        maze_line = ""
        for col in range(w):
            if (row,col) in optimal:
                maze_line += "O"
            elif (row, col) in walls:
                maze_line += "#"
            else:
                maze_line += "."
        print(maze_line)



start_time = time()
touched = set()
walls = set()
done = set()
maze = {}
start_state = ((0, 0), (0, 1))
end_state = (0, 0)
maze_ways = {}
for i, ln in enumerate(open('input_16.txt', 'r', encoding='utf-8')):
    lin = ln.strip()
    for j in range(len(lin)):
        ps = (i, j)
        if lin[j] == ".":
            maze[(ps, (-1, 0))] = 140 * 140 * 1000 * 1000
            maze[(ps, (1, 0))] = 140 * 140 * 1000 * 1000
            maze[(ps, (0, -1))] = 140 * 140 * 1000 * 1000
            maze[(ps, (0, 1))] = 140 * 140 * 1000 * 1000
            maze_ways[ps] = []
        elif lin[j] == "S":
            maze[(ps, (-1, 0))] = 140 * 140 * 1000 * 1000
            maze[(ps, (1, 0))] = 140 * 140 * 1000 * 1000
            maze[(ps, (0, -1))] = 140 * 140 * 1000 * 1000
            maze[(ps, (0, 1))] = 0
            start_state = (ps, (0, 1))
            way = set()
            way.add(ps)
            maze_ways[ps] = []
            maze_ways[ps].append(way)
        elif lin[j] == "E":
            maze[(ps, (-1, 0))] = 140 * 140 * 1000 * 1000
            maze[(ps, (1, 0))] = 140 * 140 * 1000 * 1000
            maze[(ps, (0, -1))] = 140 * 140 * 1000 * 1000
            maze[(ps, (0, 1))] = 140 * 140 * 1000 * 1000
            maze_ways[ps] = []
            end_state = ps
        elif lin[j] == "#":
            walls.add((i, j))
maze_size = i + 1
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
print(answer_part_1)
optimal = set()
for way in maze_ways[end_state]:
    optimal = optimal.union(way)
answer_part_2  = len(optimal)
print(answer_part_2)
draw_maze(maze_size, maze_size)
print("Elapsed time: %s seconds" % round(time() - start_time, 3))

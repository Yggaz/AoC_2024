import heapq
from copy import deepcopy
from time import time

def draw_maze():
    global N, source, target
    for row in range(N):
        maze_line = ""
        for col in range(N):
            if (row, col) == source:
                maze_line += "S"
            elif (row, col) == target:
                maze_line += "E"
            elif (row,col) in path:
                maze_line += "O"
            elif (row, col) in walls:
                maze_line += "#"
            else:
                maze_line += "."
        print(maze_line)


start_time = time()
walls, path = set(), set()
data = open('input_20.txt', 'r', encoding='utf-8').read()
for x, line in enumerate(data.split()):
    for y, c in enumerate(line.strip()):
        match c:
            case '#': walls.add((x, y))
            case 'S': source = (x, y)
            case 'E': target = (x,y)
N = x + 1
done = set()
cost = 0
path = [source]
que = [(cost, source, path)]
while que:
    cost, pos, path = heapq.heappop(que)
    if pos == target:
        break
    if pos in done:
        continue
    done.add(pos)
    x, y = pos
    tmp = deepcopy(path)
    tmp.append(pos)
    if (x - 1, y) not in walls:
        heapq.heappush(que, (cost + 1, (x - 1, y), tmp))
    if (x + 1, y) not in walls:
        heapq.heappush(que, (cost + 1, (x + 1, y), tmp))
    if (x, y - 1) not in walls:
        heapq.heappush(que, (cost + 1, (x, y - 1), tmp))
    if (x, y + 1) not in walls:
        heapq.heappush(que, (cost + 1, (x, y + 1), tmp))
base_cost = cost
draw_maze()
print('Target cost with all walls', base_cost)
print("Elapsed time: %s seconds" % round(time() - start_time, 3))


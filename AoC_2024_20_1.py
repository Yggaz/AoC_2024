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
limit = 100
walls = set()
path = []
data = open('input_20.txt', 'r', encoding='utf-8').read()
for x, line in enumerate(data.split()):
    for y, c in enumerate(line.strip()):
        match c:
            case '#': walls.add((x, y))
            case 'S': source = (x, y)
            case 'E': target = (x,y)
N = x + 1
path.append(source)
cur = source
while cur != target:
    x, y = cur
    if (x - 1, y) not in walls and (x - 1, y) not in path:
        cur = (x - 1, y)
    elif (x + 1, y) not in walls and (x + 1, y) not in path:
        cur = (x + 1, y)
    elif (x, y - 1) not in walls and (x, y - 1) not in path:
        cur = (x, y - 1)
    elif (x, y + 1) not in walls and (x, y + 1) not in path:
        cur = (x, y + 1)
    else:
        break
    path.append(cur)
base_cost = len(path) - 1
print('Сost with all walls', base_cost)
effective = 0
for step in path:
    x, y = step
    pos1 = path.index(step)
    if (x+2, y) in path and path.index((x+2, y)) - pos1 > limit + 1:
        effective +=1
    if (x-2, y) in path and path.index((x-2, y)) - pos1 > limit + 1:
        effective +=1
    if (x, y+2) in path and path.index((x, y+2)) - pos1 > limit + 1:
        effective +=1
    if (x, y-2) in path and path.index((x, y-2)) - pos1 > limit + 1:
        effective +=1

    if (x+1, y+1) in path and path.index((x+1, y+1)) - pos1 > limit + 1:
        effective +=2
    if (x-1, y-1) in path and path.index((x-1, y-1)) - pos1 > limit + 1:
        effective +=2
    if (x+1, y-1) in path and path.index((x+1, y-1)) - pos1 > limit + 2:
        effective +=2
    if (x-1, y+1) in path and path.index((x-1, y+1)) - pos1 > limit + 2:
        effective +=2
print("Part 1 answer:", effective)
print("Elapsed time: %s seconds" % round(time() - start_time, 3))

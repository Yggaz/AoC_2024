def blocked(x, y, dx, dy) -> bool:
    res = False
    if (x + dx, y + dy) in walls:
        res = True
    elif (x + dx, y + dy) in boxes:
        res = blocked(x + dx, y + dy, dx, dy)
    else:
        res = False
    return res

def move_robot(cmd):
    if cmd == "^":
        dx, dy = -1, 0
    if cmd == "v":
        dx, dy = 1, 0
    if cmd == ">":
        dx, dy = 0, 1
    if cmd == "<":
        dx, dy = 0, -1
    if not blocked(robot[0], robot[1], dx, dy):
        robot[0] += dx
        robot[1] += dy
        if (robot[0], robot[1]) in boxes:
            move_box(robot[0], robot[1], dx, dy)

def move_box(x, y, dx, dy):
    r = boxes.index((x, y))
    if (x+dx, y+dy) in boxes:
        move_box(x+dx, y+dy, dx, dy)
    boxes[r] = (x+dx, y+dy)


walls = set()
boxes = []
cmds = []
read_maze = True
size = 0
robot = [0, 0]
for i, ln in enumerate(open('input_15.txt', 'r', encoding='utf-8')):
    lin = ln.strip()
    if len(lin) == 0:
        read_maze = False
    if read_maze:
        for j in range(len(lin)):
            if lin[j] == "#":
                walls.add((i, j))
            elif lin[j] == "O":
                boxes.append((i, j))
            elif lin[j] == "@":
                robot[0] = i
                robot[1] = j
    else:
        for j in range(len(lin)):
            cmds.append(lin[j])
for c in cmds:
    move_robot(c)
s1 = sum(b[0]*100 + b[1] for b in boxes)
print(s1)

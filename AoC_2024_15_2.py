def blocked(x, y, dx, dy) -> bool:
    res = False
    if (x + dx, y + dy) in walls:
        res = True
    elif (x + dx, y + dy) in boxes_l:
        ind = boxes_l.index((x + dx, y + dy))
        res = blocked_box(ind, dx, dy)
    elif (x + dx, y + dy) in boxes_r:
        ind = boxes_r.index((x + dx, y + dy))
        res = blocked_box(ind, dx, dy)
    else:
        res = False
    return res

def blocked_box(n, dx, dy) -> bool:
    res = False
    if (boxes_l[n][0] + dx, boxes_l[n][1] + dy) in walls:
        res = True
    elif (boxes_r[n][0] + dx, boxes_r[n][1] + dy) in walls:
        res = True
    else:
        if (boxes_l[n][0] + dx, boxes_l[n][1] + dy) in boxes_l:
            ind = boxes_l.index((boxes_l[n][0] + dx, boxes_l[n][1] + dy))
            if ind != n:
                res = res or blocked_box(ind, dx, dy)
        if (boxes_r[n][0] + dx, boxes_r[n][1] + dy) in boxes_l:
            ind = boxes_l.index((boxes_r[n][0] + dx, boxes_r[n][1] + dy))
            if ind != n:
                res = res or blocked_box(ind, dx, dy)
        if (boxes_l[n][0] + dx, boxes_l[n][1] + dy) in boxes_r:
            ind = boxes_r.index((boxes_l[n][0] + dx, boxes_l[n][1] + dy))
            if ind != n:
                res = res or blocked_box(ind, dx, dy)
        if (boxes_r[n][0] + dx, boxes_r[n][1] + dy) in boxes_r:
            ind = boxes_r.index((boxes_r[n][0] + dx, boxes_r[n][1] + dy))
            if ind != n:
                res = res or blocked_box(ind, dx, dy)
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
        if (robot[0], robot[1]) in boxes_l:
            ind = boxes_l.index((robot[0], robot[1]))
            move_box(ind, dx, dy)
        elif (robot[0], robot[1]) in boxes_r:
            ind = boxes_r.index((robot[0], robot[1]))
            move_box(ind, dx, dy)

def move_box(n, dx, dy):
    xl, yl = boxes_l[n]
    xr, yr = boxes_r[n]
    if (xl + dx, yl + dy) in boxes_l:
        ind_l = boxes_l.index((xl + dx, yl + dy))
        if ind_l != n:
            move_box(ind_l, dx, dy)
    if (xl + dx, yl + dy) in boxes_r:
        ind_r = boxes_r.index((xl + dx, yl + dy))
        if ind_r != n:
            move_box(ind_r, dx, dy)
    if (xr + dx, yr + dy) in boxes_l:
        ind_l = boxes_l.index((xr + dx, yr + dy))
        if ind_l != n:
            move_box(ind_l, dx, dy)
    if (xr + dx, yr + dy) in boxes_r:
        ind_r = boxes_r.index((xr + dx, yr + dy))
        if ind_r != n:
            move_box(ind_r, dx, dy)
    boxes_l[n] = (xl + dx, yl + dy)
    boxes_r[n] = (xr + dx, yr + dy)

def draw_maze(w, h):
    for i in range(h):
        ln = ""
        for j in range(w):
            if (i, j) in walls:
                ln += "#"
            elif (i,j) in boxes_l:
                ln += "["
            elif (i,j) in boxes_r:
                ln += "]"
            elif (i, j) == (robot[0], robot[1]):
                ln += "@"
            else:
                ln += "."
        print(ln)

def check_box() -> int:
    res = -1
    for i in range(len(boxes_l)):
        if boxes_l[i] in walls or boxes_r[i] in walls:
            res = i
            break
    return res


walls = set()
boxes_l = []
boxes_r = []
cmds = []
read_maze = True
size = 0
robot = [0, 0]
for i, ln in enumerate(open('input_15.txt', 'r', encoding='utf-8')):
    lin = ln.strip()
    if len(lin) == 0:
        read_maze = False
    if read_maze:
        size += 1
        col = 0
        for j in range(len(lin)):
            if lin[j] == "#":
                walls.add((i, col))
                walls.add((i, col + 1))
            elif lin[j] == "O":
                boxes_l.append((i, col))
                boxes_r.append((i, col + 1))
            elif lin[j] == "@":
                robot[0] = i
                robot[1] = col
            col += 2
    else:
        for j in range(len(lin)):
            cmds.append(lin[j])

print("Start!")
draw_maze(col, size)
for step, c in enumerate(cmds):
    move_robot(c)
    # ch = check_box()
    # if ch > 0:
    #     print("step: " + str(step))
    #     print("cmd: " + c)
    #     print("Bad box %d: (%d, %d) - (%d, %d)" % (ch, boxes_l[ch][0], boxes_l[ch][1], boxes_r[ch][0], boxes_r[ch][1]))
    #     draw_maze(col, size)
    #     break
print("End!")
draw_maze(col, size)
s2 = sum(b[0]*100 + b[1] for b in boxes_l)
print(s2)




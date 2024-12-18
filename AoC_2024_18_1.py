import heapq
N = 70
part_1_limit = 1024
wall_list = []
walls = set()
for i, ln in enumerate(open('input_18.txt', 'r', encoding='utf-8')):
    wl = tuple(map(int, ln.strip().split(',')))
    wall_list.append(wl)
    if i < part_1_limit:
        walls.add(wl)
exit_reachable = True
step = part_1_limit - 1
while exit_reachable:
    done = set()
    pos = (0, 0)
    finish = (N, N)
    cost = 0
    q = [(cost, pos)]
    while q:
        cost, pos = heapq.heappop(q)
        if pos == finish:
            break
        if pos in done:
            continue
        done.add(pos)
        x, y = pos
        if x > 0 and (x-1, y) not in walls:
            heapq.heappush(q, (cost + 1, (x - 1, y)))
        if x < N and (x+1, y) not in walls:
            heapq.heappush(q, (cost + 1, (x + 1, y)))
        if y > 0 and (x, y-1) not in walls:
            heapq.heappush(q, (cost + 1, (x, y - 1)))
        if y < N and (x, y+1) not in walls:
            heapq.heappush(q, (cost + 1, (x, y + 1)))
    exit_reachable = pos == finish
    if step == part_1_limit - 1:
        print('Part 1 answer:', cost)
    if exit_reachable:
        step += 1
        walls.add(wall_list[step])
    else:
        print('Part 2 answer: %d,%d'% (wall_list[step][0], wall_list[step][1]))

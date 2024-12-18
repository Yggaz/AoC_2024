import heapq

def get_walls(how_many: int) -> set:
    tmp = set()
    for s in range(how_many):
        tmp.add(wall_list[s])
    return tmp

def blocked(how_many) -> bool:
    global N, part_1_limit
    walls = get_walls(how_many)
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
    if how_many == part_1_limit:
        print('Part 1 answer: %d' % cost)
    return pos == finish

N = 70
part_1_limit = 1024
wall_list = []
for ln in open('input_18.txt', 'r', encoding='utf-8'):
    wall_list.append(tuple(map(int, ln.strip().split(','))))
reachable = part_1_limit
blocked(reachable)
unreachable = len(wall_list)
while reachable + 1 < unreachable:
    tst = (reachable + unreachable) // 2
    if blocked(tst):
        reachable = tst
    else:
        unreachable = tst
print('Part 2 answer: %d,%d' % (wall_list[reachable][0], wall_list[reachable][1]))

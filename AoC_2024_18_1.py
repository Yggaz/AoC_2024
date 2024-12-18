import heapq

def draw_maze(bytes):
    global N
    for i in range(N+1):
        ln = ''
        for j in range(N+1):
            if (i, j) in walls:
                ln += '#'
            else:
                ln += '.'
        print(ln)

N = 70
part_1_limit = 1024
walls = set()
done = set()
for i, ln in enumerate(open('input_18.txt', 'r', encoding='utf-8')):
    if i < part_1_limit:
        wallr = tuple(map(int, ln.strip().split(',')))
        wall = (wallr[1], wallr[0])
        walls.add(wall)
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
if pos == finish:
    draw_maze(part_1_limit)
print(cost)

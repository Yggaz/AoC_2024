class region:
    def __init__(self, t, x, y, k):
        self.plant_type = t
        self.num = k
        self.plants = set()
        self.plants.add((i, j))
        touched.add((i, j))
        prev = 0
        while len(self.plants) - prev > 0:
            prev = len(self.plants)
            tmp = set()
            for c in self.plants:
                x = c[0]
                y = c[1]
                dx1 = x - 1 if x > 0 else x
                dx2 = x + 1 if x < N - 1 else x
                dy1 = y - 1 if y > 0 else y
                dy2 = y + 1 if y < N - 1 else y
                if farm[x][dy1] == t:
                    tmp.add((x, dy1))
                    touched.add((x, dy1))
                if farm[x][dy2] == t:
                    tmp.add((x, dy2))
                    touched.add((x, dy2))
                if farm[dx1][y] == t:
                    tmp.add((dx1, y))
                    touched.add((dx1, y))
                if farm[dx2][y] == t:
                    tmp.add((dx2, y))
                    touched.add((dx2, y))
            self.plants = self.plants.union(tmp)


    def surface(self) -> int:
        return len(self.plants)

    def perimeter(self) -> int:
        s = 0
        for c in self.plants:
            x = c[0]
            y = c[1]
            s += 0 if (x, y - 1) in self.plants else 1
            s += 0 if (x, y + 1) in self.plants else 1
            s += 0 if (x + 1, y) in self.plants else 1
            s += 0 if (x - 1, y) in self.plants else 1
        return s


N = 0
farm = []
regions = []
touched = set()
k = 0
for ln in open('input_12.txt', 'r', encoding='utf-8'):
    if N == 0:
        N = len(ln) - 1
    farm.append(ln)
for i in range(N):
    for j in range(N):
        if (i, j) not in touched:
            r = region(farm[i][j], i, j, k)
            k += 1
            regions.append(r)
res = sum (reg.surface() * reg.perimeter() for reg in regions)
print(res)

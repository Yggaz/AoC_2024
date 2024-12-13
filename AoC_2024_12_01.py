class Region:
    def __init__(self, t, xx, yy):
        self.plant_type = t
        self.plants = set()
        self.plants.add((xx, yy))
        touched.add((xx, yy))
        cur_layer = self.plants
        self.tBorders = {}
        self.bBorders = {}
        self.lBorders = {}
        self.rBorders = {}
        prev = 0
        while len(self.plants) - prev > 0:
            prev = len(self.plants)
            tmp = set()
            for c in cur_layer:
                x, y = c
                if x > 0:
                    if farm[x - 1][y] == t:
                        tmp.add((x - 1, y))
                        touched.add((x - 1, y))
                    else:
                        self.tBorders[(x, y)] = 2
                else:
                    self.tBorders[(x, y)] = 2
                if x < N - 1:
                    if farm[x + 1][y] == t:
                        tmp.add((x + 1, y))
                        touched.add((x + 1, y))
                    else:
                        self.bBorders[(x, y)] = 2
                else:
                    self.bBorders[(x, y)] = 2
                if y > 0:
                    if farm[x][y - 1] == t:
                        tmp.add((x, y - 1))
                        touched.add((x, y - 1))
                    else:
                        self.lBorders[(x, y)] = 2
                else:
                    self.lBorders[(x, y)] = 2
                if y < N - 1:
                    if farm[x][y + 1] == t:
                        tmp.add((x, y + 1))
                        touched.add((x, y + 1))
                    else:
                        self.rBorders[(x, y)] = 2
                else:
                    self.rBorders[(x, y)] = 2
            cur_layer = tmp
            self.plants = self.plants.union(tmp)
        for k in self.tBorders.keys():
            x, y = k
            if (x, y - 1) in self.tBorders.keys():
                self.tBorders[(x, y)] = self.tBorders.get((x, y), 0) - 1
            if (x, y + 1) in self.tBorders.keys():
                self.tBorders[(x, y)] = self.tBorders.get((x, y), 0) - 1
        for k in self.bBorders.keys():
            x, y = k
            if (x, y - 1) in self.bBorders.keys():
                self.bBorders[(x, y)] = self.bBorders.get((x, y), 0) - 1
            if (x, y + 1) in self.bBorders.keys():
                self.bBorders[(x, y)] = self.bBorders.get((x, y), 0) - 1
        for k in self.lBorders.keys():
            x, y = k
            if (x - 1, y) in self.lBorders.keys():
                self.lBorders[(x, y)] = self.lBorders.get((x, y), 0) - 1
            if (x + 1, y) in self.lBorders.keys():
                self.lBorders[(x, y)] = self.lBorders.get((x, y), 0) - 1
        for k in self.rBorders.keys():
            x, y = k
            if (x - 1, y) in self.rBorders.keys():
                self.rBorders[(x, y)] = self.rBorders.get((x, y), 0) - 1
            if (x + 1, y) in self.rBorders.keys():
                self.rBorders[(x, y)] = self.rBorders.get((x, y), 0) - 1


    def surface(self) -> int:
        return len(self.plants)

    def perimeter(self) -> int:
        return len(self.tBorders.keys()) + len(self.bBorders.keys()) + len(self.rBorders.keys()) + len(self.lBorders.keys())

    def cnt_top(self) -> int:
        return sum(self.tBorders[cl] for cl in self.tBorders.keys()) // 2

    def cnt_bottom(self) -> int:
        return sum(self.bBorders[cl] for cl in self.bBorders.keys()) // 2

    def cnt_left(self) -> int:
        return sum(self.lBorders[cl] for cl in self.lBorders.keys()) // 2

    def cnt_right(self) -> int:
        return sum(self.rBorders[cl] for cl in self.rBorders.keys()) // 2

    def cnt_sides(self) -> int:
        return self.cnt_top() + self.cnt_bottom() + self.cnt_left() + self.cnt_right()


N = 0
farm = []
regions = []
touched = set()
for ln in open('input_12.txt', 'r', encoding='utf-8'):
    if N == 0:
        N = len(ln) - 1
    farm.append(ln)
for i in range(N):
    for j in range(N):
        if (i, j) not in touched:
            r = Region(farm[i][j], i, j)
            regions.append(r)
res = sum (reg.surface() * reg.perimeter() for reg in regions)
res2 = sum (reg.surface() * reg.cnt_sides() for reg in regions)
print(res)
print(res2)

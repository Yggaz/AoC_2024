class region:
    def __init__(self, t, x, y, k):
        self.plant_type = t
        self.id = k
        self.plants = set()
        self.top = i
        self.bottom = i
        self.left = j
        self.right = j
        self.plants.add((i, j))
        touched.add((i, j))
        prev = 0
        while len(self.plants) - prev > 0:
            prev = len(self.plants)
            tmp = set()
            for c in self.plants:
                x, y = c
                dy1 = y - 1 if y > 0 else y
                dy2 = y + 1 if y < N - 1 else y
                dx1 = x - 1 if x > 0 else x
                dx2 = x + 1 if x < N - 1 else x
                if farm[x][dy1] == t:
                    tmp.add((x, dy1))
                    touched.add((x, dy1))
                    if self.left > dy1:
                        self.left = dy1
                if farm[x][dy2] == t:
                    tmp.add((x, dy2))
                    touched.add((x, dy2))
                    if self.right < dy2:
                        self.right = dy2
                if farm[dx1][y] == t:
                    tmp.add((dx1, y))
                    touched.add((dx1, y))
                    if self.top > dx1:
                        self.top = dx1
                if farm[dx2][y] == t:
                    tmp.add((dx2, y))
                    touched.add((dx2, y))
                    if self.bottom < dx2:
                        self.bottom = dx2
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

    def cnt_top(self) -> int:
        res = 0
        for l in range(self.top, self.bottom + 1):
            tmp_line = set()
            tmp_dict = {}
            for c in range(self.left, self.right + 1):
                if (l, c) in self.plants and (l - 1, c) not in self.plants:
                    tmp_line.add((l, c))
                    tmp_dict[(l, c)] = 0
            for cell in tmp_line:
                x = cell[0]
                y = cell[1]
                if (x, y-1) in tmp_line:
                    tmp_dict[cell] = tmp_dict.get(cell, 0) + 1
                if (x, y + 1) in tmp_line:
                    tmp_dict[cell] = tmp_dict.get(cell, 0) + 1
            res += len(tmp_dict.keys()) - sum(tmp_dict[cl] for cl in tmp_dict.keys()) // 2
        return res


    def cnt_bottom(self) -> int:
        res = 0
        for l in range(self.top, self.bottom + 1):
            tmp_line = set()
            tmp_dict = {}
            for c in range(self.left, self.right + 1):
                if (l, c) in self.plants and (l + 1, c) not in self.plants:
                    tmp_line.add((l, c))
                    tmp_dict[(l, c)] = 0
            for cell in tmp_line:
                x = cell[0]
                y = cell[1]
                if (x, y-1) in tmp_line:
                    tmp_dict[cell] = tmp_dict.get(cell, 0) + 1
                if (x, y + 1) in tmp_line:
                    tmp_dict[cell] = tmp_dict.get(cell, 0) + 1
            res += len(tmp_dict.keys()) - sum(tmp_dict[cl] for cl in tmp_dict.keys()) // 2
        return res

    def cnt_left(self) -> int:
        res = 0
        for c in range(self.left, self.right + 1):
            tmp_col = set()
            tmp_dict = {}
            for l in range(self.top, self.bottom + 1):
                if (l, c) in self.plants and (l, c - 1) not in self.plants:
                    tmp_col.add((l, c))
                    tmp_dict[(l, c)] = 0
            for cell in tmp_col:
                x = cell[0]
                y = cell[1]
                if (x-1, y) in tmp_col:
                    tmp_dict[cell] = tmp_dict.get(cell, 0) + 1
                if (x+1, y) in tmp_col:
                    tmp_dict[cell] = tmp_dict.get(cell, 0) + 1
            res += len(tmp_dict.keys()) - sum(tmp_dict[cl] for cl in tmp_dict.keys()) // 2
        return res

    def cnt_right(self) -> int:
        res = 0
        for c in range(self.left, self.right + 1):
            tmp_col = set()
            tmp_dict = {}
            for l in range(self.top, self.bottom + 1):
                if (l, c) in self.plants and (l, c + 1) not in self.plants:
                    tmp_col.add((l, c))
                    tmp_dict[(l, c)] = 0
            for cell in tmp_col:
                x = cell[0]
                y = cell[1]
                if (x-1, y) in tmp_col:
                    tmp_dict[cell] = tmp_dict.get(cell, 0) + 1
                if (x+1, y) in tmp_col:
                    tmp_dict[cell] = tmp_dict.get(cell, 0) + 1
            res += len(tmp_dict.keys()) - sum(tmp_dict[cl] for cl in tmp_dict.keys()) // 2
            #print(tmp_c.keys())
        return res

    def cnt_sides(self) -> int:
        return self.cnt_top() + self.cnt_bottom() + self.cnt_left() + self.cnt_right()



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
res2 = sum (reg.surface() * reg.cnt_sides() for reg in regions)
print(res)
print(res2)

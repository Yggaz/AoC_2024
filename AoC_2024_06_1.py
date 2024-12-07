import time
class Sentry:
    def __init__(self, nrow=-1, ncol=-1):
        i = 0
        j = 0
        cur = maze[i][j]
        while cur not in ('>','<','^','v'):
            j += 1
            if j == N:
                j = 0
                i+= 1
            cur = maze[i][j]
        self.row = i
        self.col = j
        if nrow == i and ncol == j:
            self.newr = -1
            self.newc = -1
        else:
            self.newr = nrow
            self.newc = ncol
        self.dir = cur
        self.out = False
        self.cycle = False
        self.steps = set()
        self.state = set()


    def step(self):
        st = tuple((self.row, self.col, self.dir))
        if st in self.state:
            self.cycle = True
            self.out = True
        else:
            self.state.add(st)
        self.steps.add(tuple((self.row, self.col)))
        if self.dir == '>':
            if self.col == N - 1:
                self.out = True
            else:
                if maze[self.row][self.col + 1] == '#' or (self.row == self.newr and self.col + 1 == self.newc):
                    self.dir = 'v'
                else:
                    self.col += 1
        elif self.dir == 'v':
            if self.row == N - 1:
                self.out = True
            else:
                if maze[self.row + 1][self.col] == '#' or (self.row + 1 == self.newr and self.col == self.newc):
                    self.dir = '<'
                else:
                    self.row += 1
        elif self.dir == '<':
            if self.col == 0:
                self.out = True
            else:
                if maze[self.row][self.col - 1] == '#' or (self.row == self.newr and self.col - 1 == self.newc):
                    self.dir = '^'
                else:
                    self.col -= 1
        elif self.dir == '^':
            if self.row == 0:
                self.out = True
            else:
                if maze[self.row - 1][self.col] == '#' or (self.row - 1 == self.newr and self.col == self.newc):
                    self.dir = '>'
                else:
                    self.row -= 1


start_time = time.time()
f_in = open('input_06.txt', 'r', encoding='utf-8')
maze = f_in.readlines()
f_in.close()
N = len(maze)
s = Sentry()
while not s.out:
    s.step()
print(len(s.steps))
cycles = 0
for tt in s.steps:
    sen = Sentry(tt[0], tt[1])
    while not sen.out:
        sen.step()
        if sen.cycle:
            cycles += 1
print(cycles)
print("--- %s seconds ---" % round(time.time() - start_time, 3))

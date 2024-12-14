class Robot:
    def __init__(self, x: int, y: int, dx: int, dy: int):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def tick(self):
        global H
        global W
        self.x += self.dx
        self.x = self.x % W
        self.y += self.dy
        self.y = self.y % H


    def quad(self) -> int:
        global H
        global W
        res = 0
        if self.x < W // 2 and self.y < H // 2:
            res = 1
        elif self.x < W // 2 and self.y > H // 2:
            res = 2
        elif self.x > W // 2 and self.y < H // 2:
            res = 3
        elif self.x > W // 2 and self.y > H // 2:
            res = 4
        return res

H = 103
W = 101
robots = []
s = [0, 0, 0, 0, 0]
for ln in open('input_14.txt', 'r', encoding='utf-8'):
    lin = ln.split()
    ps = lin[0].split(",")
    vl = lin[1].split(",")
    r = Robot(int(ps[0][2:]), int(ps[1]), int(vl[0][2:]), int(vl[1]))
    for i in range(100):
        r.tick()
    s[r.quad()] += 1
    robots.append(r)
print(s[1]*s[2]*s[3]*s[4])

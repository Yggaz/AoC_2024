from PIL import Image, ImageDraw
from time import time
class Robot:
    def __init__(self, x: int, y: int, dx: int, dy: int):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

class Robots:
    def __init__(self, h: int, w: int, p: int, l:int):
        self.H = h
        self.W = w
        self.ticks = 0
        self.prints = p
        self.tick_limit = l
        self.largest = 0
        self.robots = []

    def add_robot(self, x: int, y: int, dx: int, dy: int):
        r = Robot(x, y, dx, dy)
        self.robots.append(r)

    def finished(self) -> bool:
        return (self.prints == 0) or (self.ticks >= self.tick_limit)

    def pict(self):
        image = Image.new("RGB", (self.H, self.W), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        name = "./" + str(self.ticks).zfill(5) + ".png"
        for r in self.robots:
            draw.point((r.x, r.y), (255,255,255))
        image.save(name, "PNG")
        self.largest = 0
        self.prints -= 1


    def tick(self):
        self.ticks += 1
        rpos = {}
        for r in self.robots:
            r.x += r.dx
            r.x = r.x % self.W
            r.y += r.dy
            r.y = r.y % self.H
            rpos[(r.x, r.y)] = rpos.get((r.x, r.y), 0) + 1
        touched = set()
        for k in rpos.keys():
            if k not in touched:
                touched.add(k)
                cur = set()
                cur.add(k)
                prev = 0
                while len(cur) > prev:
                    prev = len(cur)
                    nxt = set()
                    for c in cur:
                        xx = c[0]
                        yy = c[1]
                        if (xx-1, yy) not in touched and (xx-1, yy) in rpos.keys():
                            nxt.add((xx-1, yy))
                            touched.add((xx - 1, yy))
                        if (xx+1, yy) not in touched and (xx+1, yy) in rpos.keys():
                            nxt.add((xx+1, yy))
                            touched.add((xx + 1, yy))
                        if (xx, yy-1) not in touched and (xx, yy-1) in rpos.keys():
                            nxt.add((xx, yy-1))
                            touched.add((xx, yy - 1))
                        if (xx, yy+1) not in touched and (xx, yy+1) in rpos.keys():
                            nxt.add((xx, yy+1))
                            touched.add((xx, yy + 1))
                    cur = cur.union(nxt)
                s = sum(rpos[k] for k in cur)
                if s > self.largest:
                    self.largest = s
        if self.largest > 100:
            print(self.ticks)
            self.pict()


start_time = time()
allR = Robots(103, 101, 1, 10000)
for ln in open('input_14.txt', 'r', encoding='utf-8'):
    lin = ln.split()
    ps = lin[0].split(",")
    vl = lin[1].split(",")
    allR.add_robot(int(ps[0][2:]), int(ps[1]), int(vl[0][2:]), int(vl[1]))
while not allR.finished():
    allR.tick()
if allR.prints == 0:
    print("All images found!")
else:
    print("Tick limit reached!")
print("Elapsed time: %s seconds" % round(time() - start_time, 3))

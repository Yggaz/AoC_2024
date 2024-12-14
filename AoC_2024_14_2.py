from PIL import Image, ImageDraw
class Robot:
    def __init__(self, x: int, y: int, dx: int, dy: int):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

class Robots:
    def __init__(self, h: int, w: int):
        self.H = h
        self.W = w
        self.ticks = 0
        self.robots = []

    def add_robot(self, x: int, y: int, dx: int, dy: int):
        r = Robot(x, y, dx, dy)
        self.robots.append(r)

    def pict(self):
        image = Image.new("RGB", (self.H, self.W), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        name = "./images14/" + str(self.ticks).zfill(5) + ".png"
        for r in self.robots:
            draw.point((r.x, r.y), (255,255,255))
        image.save(name, "PNG")

    def tick(self):
        self.ticks += 1
        for r in self.robots:
            r.x += r.dx
            r.x = r.x % self.W
            r.y += r.dy
            r.y = r.y % self.H
        self.pict()



allR = Robots(103, 101)
for ln in open('input_14.txt', 'r', encoding='utf-8'):
    lin = ln.split()
    ps = lin[0].split(",")
    vl = lin[1].split(",")
    allR.add_robot(int(ps[0][2:]), int(ps[1]), int(vl[0][2:]), int(vl[1]))
while True:
    allR.tick()
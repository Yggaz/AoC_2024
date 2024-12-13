from math import gcd

class Machine:
    def __init__(self, a: tuple, b: tuple, p: tuple):
        self.butA = a
        self.butB = b
        # q = p
        q = (p[0] + 10000000000000, p[1] + 10000000000000)
        self.prize = q
        self.press_b = a[0] * q[1] - a[1] * q[0]
        self.press_a = b[1] * q[0] - b[0] * q[1]
        if self.press_b < 0 and self.press_a < 0:
            self.press_b, self.press_a = -self.press_b, -self.press_a
        step = gcd(self.press_b, self.press_a)
        self.press_b, self.press_a = self.press_b // step, self.press_a // step
        steps = q[0] // (self.press_a * a[0] + self.press_b * b[0])
        self.press_b, self.press_a = self.press_b * steps, self.press_a * steps



machines = []
but_a = (0, 0)
but_b = (0, 0)
for ln in open('input_13.txt', 'r', encoding='utf-8'):
    lin = ln.split(":")
    if len(lin) == 2:
        if lin[0] == "Button A":
            bb = lin[1].split(", ")
            but_a = (int(bb[0][2:]), int(bb[1][2:]))
        elif lin[0] == "Button B":
            bb = lin[1].split(", ")
            but_b = (int(bb[0][2:]), int(bb[1][2:]))
        else:
            bb = lin[1].split(", ")
            prize = (int(bb[0][3:]), int(bb[1][2:]))
            m = Machine(but_a, but_b, prize)
            machines.append(m)
s = 0
for m in machines:
    if 0 < m.press_a and 0 < m.press_b:
        s += m.press_a * 3 + m.press_b
print(s)
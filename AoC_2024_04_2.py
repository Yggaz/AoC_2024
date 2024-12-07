from itertools import product as p


def x_mas(i: int, j: int) -> int:
    res = 0
    if text[i][j] == 'A':
        t1 = text[i - 1][j - 1] + text[i + 1][j + 1]
        t2 = text[i + 1][j - 1] + text[i - 1][j + 1]
        if (t1 == 'MS' or t1 == 'SM') and (t2 == 'MS' or t2 == 'SM'):
            res = 1
    return res


def x_up(i: int, j: int) -> int:
    res = 0
    if i >= 3:
        if text[i][j] + text[i - 1][j] + text[i - 2][j] + text[i - 3][j] == 'XMAS':
            res = 1
    return res


def x_down(i: int, j: int) -> int:
    res = 0
    if i < N - 3:
        if text[i][j] + text[i + 1][j] + text[i + 2][j] + text[i + 3][j] == 'XMAS':
            res = 1
    return res


def x_left(i: int, j: int) -> int:
    res = 0
    if j >= 3:
        if text[i][j] + text[i][j - 1] + text[i][j - 2] + text[i][j - 3] == 'XMAS':
            res = 1
    return res


def x_right(i: int, j: int) -> int:
    res = 0
    if j < N - 3:
        if text[i][j] + text[i][j + 1] + text[i][j + 2] + text[i][j + 3] == 'XMAS':
            res = 1
    return res


def x_upleft(i: int, j: int) -> int:
    res = 0
    if i >= 3 and j >= 3:
        if text[i][j] + text[i - 1][j - 1] + text[i - 2][j - 2] + text[i - 3][j - 3] == 'XMAS':
            res = 1
    return res


def x_downright(i: int, j: int) -> int:
    res = 0
    if i < N - 3 and j < N - 3:
        if text[i][j] + text[i + 1][j + 1] + text[i + 2][j + 2] + text[i + 3][j + 3] == 'XMAS':
            res = 1
    return res


def x_downleft(i: int, j: int) -> int:
    res = 0
    if i < N - 3 and j >= 3:
        if text[i][j] + text[i + 1][j - 1] + text[i + 2][j - 2] + text[i + 3][j - 3] == 'XMAS':
            res = 1
    return res


def x_upright(i: int, j: int) -> int:
    res = 0
    if i >= 3 and j < N - 3:
        if text[i][j] + text[i - 1][j + 1] + text[i - 2][j + 2] + text[i - 3][j + 3] == 'XMAS':
            res = 1
    return res


def x_all(i: int, j: int) -> int:
    return (x_left(i, j) +
            x_right(i, j) +
            x_up(i, j) +
            x_down(i, j) +
            x_upleft(i, j) +
            x_upright(i, j) +
            x_downleft(i, j) +
            x_downright(i, j))


f_in = open('input_04.txt', 'r', encoding='utf-8')
text = f_in.readlines()
f_in.close()
N = len(text)
xms = sum(x_all(i, j) for i, j in p(range(N), range(N)))
print(xms)
x_ms = sum(x_mas(i, j) for i, j in p(range(1, N - 1), range(1, N - 1)))
print(x_ms)

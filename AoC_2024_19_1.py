from copy import copy, deepcopy
from time import time


start_time = time()
designs = []
for i, ln in enumerate(open('input_19.txt', 'r', encoding='utf-8')):
    lin = ln.strip()
    if i == 0:
        towels = list(lin.split(', '))
    else:
        if lin:
            designs.append(lin)
indep = []
combo = dict()
for j, d in enumerate(towels):
    solved = False
    combo[d] = []
    q = [(d, [])]
    cnt = 0
    while q:
        des, sol = q.pop(-1)
        for k, t in enumerate(towels):
            if k == j:
                continue
            elif t == des:
                solved = True
                solut = deepcopy(sol)
                solut.append(t)
                if solut not in combo[d]:
                    combo[d].append(solut)
            elif t == des[:len(t)]:
                solut = deepcopy(sol)
                solut.append(t)
                q.append((des[len(t):], solut))
    if not solved:
        indep.append(d)
for k in indep:
    del combo[k]
good = []
bad = []
solutions = dict()
for j, d in enumerate(designs):
    solved = False
    solutions[d] = []
    q = [(d, [])]
    while q:
        des, sol = q.pop(-1)
        for t in indep:
            if t == des:
                solved = True
                solut = deepcopy(sol)
                solut.append(t)
                if solut not in solutions[d]:
                    (solutions[d]).append(solut)
            elif t == des[:len(t)]:
                solut = deepcopy(sol)
                solut.append(t)
                q.append((des[len(t):], solut))
    if solved:
        good.append(j)
all_solutions = []
cur_sol = []

print(len(good))
print("Elapsed time: %s seconds" % round(time() - start_time, 3))

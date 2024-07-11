import random
import time
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import numpy as np
import matplotlib.colors as mcolors

N = 10

ia = list(range(1, N + 1, 1))


def get_permutations():
    p = []
    random.seed(time.time() * 1000)
    for i in range(0, N - 1):
        x = random.randint(0, N - 2)
        mask = random.randint(0, 1)
        p.append((x, x + 1, mask))
    i = 0
    while i < len(p) - 1:
        if p[i][0] == p[i + 1][0] and p[i][1] == p[i + 1][1]:
            p.pop(i)
            continue
        i += 1
    return p


fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)
ax.set_title("Entangled Test")
permutations = get_permutations()
for i in range(0, N):
    ax.plot(0, i, 'o', c=list(mcolors.TABLEAU_COLORS.keys())[i % len(mcolors.TABLEAU_COLORS)], clip_on=False)
    ax.plot(len(permutations), i, 'o', c=list(mcolors.TABLEAU_COLORS.keys())[i % len(mcolors.TABLEAU_COLORS)], clip_on=False)
print(permutations)
for j in range(0, N):
    xs = np.ma.array([0])
    ys = np.ma.array([j])
    y = j
    x = 0
    for i, perm in enumerate(permutations):
        if perm[0] == y:
            if perm[2] == 0:
                xs = np.ma.append(xs, np.ma.masked_values([i + 0.4, i + 0.5, i + 0.6], i + 0.5))
                ys = np.ma.append(ys, np.ma.masked_values([y + 0.4, y + 0.5, y + 0.6], y + 0.5))
            y += 1
        elif perm[1] == y:
            if perm[2] == 1:
                xs = np.ma.append(xs, np.ma.masked_values([i + 0.4, i + 0.5, i + 0.6], i + 0.5))
                ys = np.ma.append(ys, np.ma.masked_values([y - 0.4, y - 0.5, y - 0.6], y - 0.5))
            y -= 1
        ys = np.ma.append(ys, y)
        xs = np.ma.append(xs, i + 1)
    ax.plot(xs, ys, c=list(mcolors.TABLEAU_COLORS.keys())[j % len(mcolors.TABLEAU_COLORS)])
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.grid(True, axis='x')
ax.set_xticklabels([])
ax.set_yticks([i for i in range(0, N)], [str(i + 1) for i in range(0, N)])
ax.set_xlim(0, len(permutations))
ax.set_ylim(-1, N)
ax.set_facecolor('aliceblue')
fig.patch.set_facecolor('aliceblue')

plt.show()

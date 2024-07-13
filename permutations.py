import random
import time
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.colors as mcolors

N = 10
x_lim = N
framerate = 40
lines = []
permutations = []


def get_permutations():
    global x_lim
    p = []
    random.seed(time.time() * 1000)
    for i in range(0, N - 1):
        x = random.randint(0, N - 2)
        mask = random.randint(0, 1)
        p.append((x, x + 1, mask))
    x_lim = len(p)
    return p


def init_plot(ax, permutations):
    for j in range(0, N):
        xs = np.ma.array([0])
        ys = np.ma.array([j])
        y = j
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
        plot = ax.plot(xs, ys, c=list(mcolors.TABLEAU_COLORS.keys())[j % len(mcolors.TABLEAU_COLORS)])
        lines.append(plot)


def animate_permutations(frame):
    global permutations
    global framerate

    for j in range(0, N):
        xs = np.ma.array([0])
        ys = np.ma.array([j])
        y = j
        for i in range(0, x_lim):
            if i < len(permutations):
                if permutations[i][0] == y:
                    if permutations[i][2] == 0 and i != len(permutations) - 1:
                        xs = np.ma.append(xs, np.ma.masked_values([i + 0.4, i + 0.5, i + 0.6], i + 0.5))
                        ys = np.ma.append(ys, np.ma.masked_values([y + 0.4, y + 0.5, y + 0.6], y + 0.5))
                    y += 1
                elif permutations[i][1] == y:
                    if permutations[i][2] == 1 and i != len(permutations) - 1:
                        xs = np.ma.append(xs, np.ma.masked_values([i + 0.4, i + 0.5, i + 0.6], i + 0.5))
                        ys = np.ma.append(ys, np.ma.masked_values([y - 0.4, y - 0.5, y - 0.6], y - 0.5))
                    y -= 1
                if i == len(permutations) - 1 and y == permutations[i][0]:
                    y += 1 * (frame / framerate - int(frame / framerate))
                    ys = np.ma.append(ys, y)
                elif i == len(permutations) - 1 and y == permutations[i][1]:
                    y -= 1 * (frame / framerate - int(frame / framerate))
                    ys = np.ma.append(ys, y)
                else:
                    ys = np.ma.append(ys, y)
            else:
                ys = np.ma.append(ys, y)
            xs = np.ma.append(xs, i + 1)

        lines[j][0].set_data(xs, ys)
    if (frame + 1) % framerate == 0 and len(permutations) != 0:
        del permutations[-1]
    return lines


def main():
    global permutations

    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    ax.set_title("Entangled Test")
    permutations = get_permutations()
    for i in range(0, N):
        ax.plot(0, i, 'o', c=list(mcolors.TABLEAU_COLORS.keys())[i % len(mcolors.TABLEAU_COLORS)], clip_on=False)
        ax.plot(len(permutations), i, 'o', c=list(mcolors.TABLEAU_COLORS.keys())[i % len(mcolors.TABLEAU_COLORS)],
                clip_on=False)
    print(permutations)
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.grid(True, axis='x')
    ax.set_xticklabels([])
    ax.set_yticks([i for i in range(0, N)], [str(i + 1) for i in range(0, N)])
    ax.set_xlim(0, len(permutations))
    ax.set_ylim(-1, N)
    ax.set_facecolor('aliceblue')
    fig.patch.set_facecolor('aliceblue')
    init_plot(ax, permutations)

    ani = FuncAnimation(fig, animate_permutations, interval=framerate, frames=len(permutations) * framerate)

    plt.show()


if __name__ == '__main__':
    main()


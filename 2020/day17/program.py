#!/usr/bin/env python3

import sys

ACTIVE = '#'


def find_active_neighbors_1(actives, i, j, k):
    n = 0
    for di in range(-1, 1 + 1):
        for dj in range(-1, 1 + 1):
            for dk in range(-1, 1 + 1):
                if not (di, dj, dk) == (0, 0, 0):
                    if (i + di, j + dj, k + dk) in actives:
                        n += 1

    return n


def advance_1(actives, mn, mx):
    new_actives = set()
    for i in range(mn, mx + 1):
        for j in range(mn, mx + 1):
            for k in range(mn, mx + 1):
                active_neighbors = find_active_neighbors_1(actives, i, j, k)
                if (i, j, k) in actives and (active_neighbors == 2 or active_neighbors == 3):
                    new_actives.add((i, j, k))
                elif (i, j, k) not in actives and active_neighbors == 3:
                    new_actives.add((i, j, k))

    return new_actives


def find_active_neighbors_2(actives, i, j, k, l):
    n = 0
    for di in range(-1, 1 + 1):
        for dj in range(-1, 1 + 1):
            for dk in range(-1, 1 + 1):
                for dl in range(-1, 1 + 1):
                    if not (di, dj, dk, dl) == (0, 0, 0, 0):
                        if (i + di, j + dj, k + dk, l + dl) in actives:
                            n += 1

    return n


def advance_2(actives, mn, mx):
    new_actives = set()
    for i in range(mn, mx + 1):
        for j in range(mn, mx + 1):
            for k in range(mn, mx + 1):
                for l in range(mn, mx + 1):
                    active_neighbors = find_active_neighbors_2(actives, i, j, k, l)
                    if (i, j, k, l) in actives and (active_neighbors == 2 or active_neighbors == 3):
                        new_actives.add((i, j, k, l))
                    elif (i, j, k, l) not in actives and active_neighbors == 3:
                        new_actives.add((i, j, k, l))

    return new_actives


def main():
    text = sys.stdin.read().splitlines()

    # Part 1
    '''
    mn = -1
    mx = len(text[0])
    a = set()
    for i, line in enumerate(text):
        for j, char in enumerate(line):
            if char == ACTIVE:
                a.add((i, j, 0))

    for _ in range(6):
        a = advance_1(a, mn, mx).copy()
        mn -= 2
        mx += 2
    print(len(a))
    '''

    # Part 2
    mn = -1
    mx = len(text[0])
    a = set()
    for i, line in enumerate(text):
        for j, char in enumerate(line):
            if char == ACTIVE:
                a.add((i, j, 0, 0))

    for _ in range(6):
        a = advance_2(a, mn, mx).copy()
        mn -= 2
        mx += 2
        print(len(a))


if __name__ == '__main__':
    main()
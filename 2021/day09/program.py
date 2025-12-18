#!/usr/bin/env python3

import sys
from pprint import pprint

numbers = [[int(x) for x in line.strip()] for line in sys.stdin.readlines()]

def get_adjacents(x, y, hlen, vlen):
    adjacents = []
    if x > 0:
        adjacents.append([x - 1, y])
    if y > 0:
        adjacents.append([x, y - 1])
    if x < vlen - 1:
        adjacents.append([x + 1, y])
    if y < hlen - 1:
        adjacents.append([x, y + 1])
    return adjacents

def find_basin_size(x, y, hlen, vlen, adjacents):
    pass

hlen = len(numbers[0])
vlen = len(numbers)

risk = 0
for i in range(vlen):
    for j in range(hlen):
        val = numbers[i][j]
        lowest = True

        adjacents = get_adjacents(i, j, hlen, vlen)
        for a in adjacents:
            if val >= numbers[a[0]][a[1]]:
                lowest = False

        if lowest:
            risk += val + 1
            s = find_basin_size(i, j, hlen, vlen, adjacents)
            print(s)

print(risk)
        
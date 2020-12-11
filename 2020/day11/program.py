#!/usr/bin/env python3

import sys
import copy
import pprint

layout_text = sys.stdin.readlines()


def adjacents(layout, x, y):
    adjs = 0
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= ny <= len(layout[0]) - 1 and 0 <= nx <= len(layout) - 1 and layout[nx][ny] == '#':
            adjs += 1
    return adjs


def fill(layout):
    new_layout = copy.deepcopy(layout)

    for i in range(len(layout)):
        for j in range(len(layout[0])):
            if layout[i][j] == 'L' and adjacents(layout, i, j) == 0:
                new_layout[i][j] = '#'
            elif layout[i][j] == '#' and adjacents(layout, i, j) >= 4:
                new_layout[i][j] = 'L'

    return new_layout


def viewadjacents(layout, x, y):
    adjs = 0
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    for i in range(8):
        nx, ny = x, y
        while 0 <= ny <= len(layout[0]) - 1 and 0 <= nx <= len(layout) - 1:
            nx, ny = nx + dx[i], ny + dy[i]
            if 0 <= ny <= len(layout[0]) - 1 and 0 <= nx <= len(layout) - 1 and layout[nx][ny] == 'L':
                break
            elif 0 <= ny <= len(layout[0]) - 1 and 0 <= nx <= len(layout) - 1 and layout[nx][ny] == '#':
                adjs += 1
                break
    return adjs


def viewfill(layout):
    new_layout = copy.deepcopy(layout)

    for i in range(len(layout)):
        for j in range(len(layout[0])):
            if layout[i][j] == 'L' and viewadjacents(layout, i, j) == 0:
                new_layout[i][j] = '#'
            elif layout[i][j] == '#' and viewadjacents(layout, i, j) >= 5:
                new_layout[i][j] = 'L'

    return new_layout


layout = []
for line in layout_text:
    line_words = []
    for word in line.strip():
        line_words.append(word)
    layout.append(line_words)

# Part 1
'''
changed = True
while changed:
    new_layout = fill(layout)
    changed = new_layout != layout
    layout = copy.deepcopy(new_layout)

noccupied = sum(row.count('#') for row in layout)
pprint.pprint(noccupied)
'''

# Part 2
changed = True
while changed:
    new_layout = viewfill(layout)
    changed = new_layout != layout
    layout = copy.deepcopy(new_layout)

noccupied = sum(row.count('#') for row in layout)
pprint.pprint(noccupied)

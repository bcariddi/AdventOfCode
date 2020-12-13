#!/usr/bin/env python3

import sys

text = sys.stdin.readlines()

# Part 1
'''
east = north = dir = 0

for line in text:
    action, value = line[0], int(line[1:])

    if action == 'N':
        north += value
    elif action == 'S':
        north -= value
    elif action == 'E':
        east += value
    elif action == 'W':
        east -= value
    elif action == 'L':
        dir += value % 360
    elif action == 'R':
        dir += (360 - value) % 360
    elif action == 'F':
        north += math.sin(math.radians(dir)) * value
        east += math.cos(math.radians(dir)) * value

print(abs(east) + abs(north))
'''

# Part 2
sx = sy = 0 # ship x and y coordinates
wx, wy = 10, 1

for line in text:
    action, value = line[0], int(line[1:])

    if action == 'N':
        wy += value
    elif action == 'S':
        wy -= value
    elif action == 'E':
        wx += value
    elif action == 'W':
        wx -= value
    elif action == 'L':
        xdiff, ydiff = wx - sx, wy - sy
        if value == 270:
            xdiff, ydiff = ydiff, -1 * xdiff
        elif value == 180:
            xdiff, ydiff = -1 * xdiff, -1 * ydiff
        elif value == 90:
            xdiff, ydiff = -1 * ydiff, xdiff
        wx, wy = sx + xdiff, sy + ydiff
    elif action == 'R':
        xdiff, ydiff = wx - sx, wy - sy
        if value == 90:
            xdiff, ydiff = ydiff, -1 * xdiff
        elif value == 180:
            xdiff, ydiff = -1 * xdiff, -1 * ydiff
        elif value == 270:
            xdiff, ydiff = -1 * ydiff, xdiff
        wx, wy = sx + xdiff, sy + ydiff
    elif action == 'F':
        xdiff, ydiff = wx - sx, wy - sy
        sx, sy = sx + value * xdiff, sy + value * ydiff
        wx, wy = sx + xdiff, sy + ydiff

print(abs(sx) + abs(sy))
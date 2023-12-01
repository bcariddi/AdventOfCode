#!/usr/bin/env python3

import sys


inp = [l.strip() for l in sys.stdin.readlines()]
compass = ['N', 'E', 'S', 'W']


def calc_distance(x, y):
    return abs(x) + abs(y)

# part 1 and 2
x = 0
y = 0
heading = 'N'

directions = [d.strip() for d in inp[0].split(',')]

seen = set()
first_repeat_distance = None

for direction in directions:
    turn = direction[0]
    dist = int(direction[1:])

    if turn == 'R':
        heading = compass[(compass.index(heading) + 1) % 4]
    else:
        heading = compass[(compass.index(heading) - 1) % 4]
  
    for _ in range(dist):
        if heading == 'N':
            y += 1
        elif heading == 'E':
            x += 1
        elif heading == 'S':
            y -= 1
        else:
            x -= 1

        if (x, y) in seen and first_repeat_distance is None:
            first_repeat_distance = calc_distance(x, y)

        seen.add((x, y))

print(f'part 1: {calc_distance(x, y)}')
print(f'part 2: {first_repeat_distance}')


#!/usr/bin/env python3

import sys

instructions = []

for line in sys.stdin:
    instructions.append(line)

# part 1

h_pos = 0
depth = 0

for instruction in instructions:
    direction, amount = instruction.split()
    amount = int(amount)

    if direction == 'forward':
        h_pos += amount
    elif direction == 'down':
        depth += amount
    elif direction == 'up':
        depth -= amount

print(h_pos * depth)

# part 2

h_pos = 0
depth = 0
aim = 0

for instruction in instructions:
    direction, amount = instruction.split()
    amount = int(amount)

    if direction == 'forward':
        h_pos += amount
        depth += aim * amount
    elif direction == 'down':
        aim += amount
    elif direction == 'up':
        aim -= amount

print(h_pos * depth)
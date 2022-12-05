#!/usr/bin/env python3

import sys
from pprint import pprint


inp = [l.rstrip() for l in sys.stdin.readlines()]


# part 1 and 2
def move(crates, n, start, dest):
    startcrate = crates[start]
    destcrate = crates[dest]

    for _ in range(n):
        element = startcrate.pop(0)
        destcrate = [element] + destcrate

    crates[start] = startcrate
    crates[dest] = destcrate

    return crates


def move2(crates, n, start, dest):
    startcrate = crates[start]
    destcrate = crates[dest]

    elements = startcrate[:n]
    startcrate = startcrate[n:]
    destcrate = elements + destcrate

    crates[start] = startcrate
    crates[dest] = destcrate

    return crates


cratelines = []
for i, line in enumerate(inp):
    if line == '':
        instructions_start_i = i
        break
    cratelines.append(line.replace('[', '').replace('] ', '').replace(']', '').replace('    ', ' '))
ncrates = int(cratelines[-1][-1])

crates = [[] for _ in range(ncrates)]

for i, line in enumerate(cratelines[:-1]):
    for j, c in enumerate(line):
        if not c.isspace():
            crates[j].append(c)

for line in inp[instructions_start_i + 1:]:
    line = line.split()
    n, start, dest = [int(x) for x in [line[1], line[3], line[5]]]
    crates = move2(crates, n, start - 1, dest - 1) # change from move2() to move() to get part 1 result

print(''.join([c[0] for c in crates if len(c)]))

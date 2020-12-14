#!/usr/bin/env python3

import sys

text = sys.stdin.readlines()
lst = [x.replace('[', ' = ').replace(']', '').strip().split(' = ') for x in text]


def compute_masked(val, mask):
    for i in range(36):
        if mask[36 - i - 1] == '1':
            val |= (1 << i)
        elif mask[36 - i - 1] == '0':
            val &= ~(1 << i)

    return val

# Part 1

memory = {}
mask = ''
for line in lst:
    if line[0] == 'mask':
        mask = line[1]
    else:
        key = int(line[1])
        val = int(line[2])
        memory[key] = compute_masked(val, mask)

tot = 0
for key in memory:
    tot += memory[key]
print(tot)


# Part 2
'''
memory = {}
mask = ''
for line in lst:
    if line[0] == 'mask':
        mask = line[1]
    else:
        key = int(line[1])
        val = int(line[2])
        # something
'''
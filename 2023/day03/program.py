#!/usr/bin/env python3

import sys
from pprint import pprint
from collections import defaultdict

SYMBOLS = '!@#$%^&*()-+='

inp = [l.strip() for l in sys.stdin.readlines()]
nrow = len(inp)
ncol = len(inp[0])

seen = set()

def get_full_number(i, j, char):
    seen.add((i, j))
    full_number = char

    pos = j - 1
    while pos > 0 and inp[i][pos].isnumeric():
        if (i, pos) in seen:
            return 0
        seen.add((i, pos))
        full_number = inp[i][pos] + full_number
        pos -= 1

    pos = j + 1
    while pos < ncol and inp[i][pos].isnumeric():
        if (i, pos) in seen:
            return 0
        seen.add((i, pos))
        full_number += inp[i][pos]
        pos += 1

    return int(full_number)


def is_adjacent(i, j):
    for x in range(-1, 2):
        if 0 <= x + i < nrow:
            for y in range(-1, 2):
                if 0 <= y + j < ncol:
                    if inp[x + i][y + j] in SYMBOLS:
                        return True
    return False


# part 1
pprint(inp)
print('-----------')

summ = 0
for i, row in enumerate(inp):
    for j, char in enumerate(row):
        if char.isnumeric() and is_adjacent(i, j):
            summ += get_full_number(i, j, char)

print(summ)

# part 2


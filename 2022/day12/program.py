#!/usr/bin/env python3

import sys
from pprint import pprint
from collections import defaultdict

START = [0, 0]
END   = [0, 0]

def convert(s):
    if s.islower():
        return ord(s) - 97
    if s == 'S':
        return 0
    return 25

inp = [l.strip() for l in sys.stdin.readlines()]

for i, l in enumerate(inp):
    for j, x in enumerate(l.strip()):
        if x == 'S':
            START = [i, j]
        if x == 'E':
            END = [i, j]

grid = [[convert(x) for x in l] for l in inp]

print(f'START:\t{START}')
print(f'END:\t{END}')


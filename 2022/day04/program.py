#!/usr/bin/env python3

import sys
from pprint import pprint
from collections import defaultdict


inp = [l.strip() for l in sys.stdin.readlines()]


def is_b_encapsulated(a1, a2, b1, b2):
    if b1 >= a1:
        if b2 <= a2:
            return 1
    return 0

def overlaps(a1, a2, b1, b2):
    if (b1 >= a1 and b1 <= a2) or (b2 >= a1 and b2 <= a2):
        return 1
    return 0

# part 1 and 2
count = 0
count2 = 0
for line in inp:
    e1, e2 = line.split(',')
    e1min, e1max = [int(x) for x in e1.split('-')]
    e2min, e2max = [int(x) for x in e2.split('-')]

    count += is_b_encapsulated(e1min, e1max, e2min, e2max) or is_b_encapsulated(e2min, e2max, e1min, e1max)
    count2 += overlaps(e1min, e1max, e2min, e2max) or overlaps(e2min, e2max, e1min, e1max)
print(count)
print(count2)

#!/usr/bin/env python3

import sys
from pprint import pprint
from collections import defaultdict


inp = sys.stdin.readlines()


# part 1
sums = []

nextsum = 0
for line in inp:
    line = line.strip()
    if len(line) == 0:
        sums.append(nextsum)
        nextsum = 0
    else:
        nextsum += int(line)

print(max(sums))

# part 2
sortedsums = sorted(sums)

print(sum(sortedsums[-3:]))


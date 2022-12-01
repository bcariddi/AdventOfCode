#!/usr/bin/env python3

''' Cleaned up version of my fast attempt '''

import sys


inp = [x.strip() for x in sys.stdin.readlines()]

# part 1
sums = []

curr_sum = 0
for line in inp:
    if not line:
        sums.append(curr_sum)
        curr_sum = 0
    else:
        curr_sum += int(line)

print(max(sums))

# part 2
sorted_sums = sorted(sums)

print(sum(sorted_sums[-3:]))


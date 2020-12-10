#!/usr/bin/env python3

import sys
import pprint
from itertools import combinations

adapters = sorted([int(x) for x in sys.stdin.readlines()])
adapters = [0] + adapters + [adapters[-1] + 3]

# Part 1
'''
onecount = 0
threecount = 0

curr = 0 # start with charging outlet
while adapters:
    diff = adapters[0] - curr

    if diff == 1:
        onecount += 1
    elif diff == 3:
        threecount += 1
    elif diff > 3:
        print('hmm...')

    curr = adapters.pop(0)

threecount += 1 # built-in adapter always has a difference of 3

print(onecount * threecount)
'''

# Part 2
dp = [None] * len(adapters)
dp[len(adapters) - 1] = 1

for i in range(len(adapters) - 2, -1, -1):
    nvalid = 0

    for j in range(i + 1, len(adapters)):
        if adapters[j] - adapters[i] > 3:
            break
        nvalid += dp[j]

    dp[i] = nvalid

tot = dp[0]
print(tot)

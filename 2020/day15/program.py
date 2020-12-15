#!/usr/bin/env python3

import sys

starting_nums = [int(x) for x in sys.stdin.read().splitlines()]

# populate dict with starting numbers
seen = {}
i = 1
for n in starting_nums:
    seen[n] = i
    i += 1

# find the last number spoken at any position
last_spoken = 0
i += 1
while i <= 30000000:
    if last_spoken in seen:
        temp = seen[last_spoken]
        seen[last_spoken] = i - 1
        last_spoken = i - 1 - temp
    else:
        seen[last_spoken] = i - 1
        last_spoken = 0
    i += 1

print(last_spoken)
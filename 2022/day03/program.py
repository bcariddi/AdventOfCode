#!/usr/bin/env python3

import sys


inp = [l.strip() for l in sys.stdin.readlines()]


def get_priority_score(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    return ord(c) - ord('A') + 27


# part 1
mysum = 0
for sack in inp:
    length = len(sack)
    fir, sec = sack[:length // 2], sack[length // 2:]

    common = (set(fir) & set(sec)).pop()
    mysum += get_priority_score(common)
print(mysum)

# part 2
mysum = 0
i = 0
for s1, s2, s3 in zip(inp, inp[1:], inp[2:]):
    if i % 3 == 0:
        common = (set(s1) & set(s2) & set(s3)).pop()
        mysum += get_priority_score(common)
    i += 1
print(mysum)

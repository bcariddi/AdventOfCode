#!/usr/bin/env python3

import sys


inp = sys.stdin.readlines()[0].strip()


def find_marker_index(inp, n):
    recent = []
    for i, c in enumerate(inp):
        if i >= n:
            if len(set(recent)) == n:
                return i
            recent.pop(0)
        recent.append(c)
    return -1


# part 1
print(find_marker_index(inp, 4))

# part 2
print(find_marker_index(inp, 14))

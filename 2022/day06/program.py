#!/usr/bin/env python3

import sys


inp = sys.stdin.readlines()[0].strip()


def find_marker_index(inp, n):
    for i, _ in enumerate(inp):
        if len(set(inp[i:i + n])) == n:
            return i + n
    return -1


# part 1
print(find_marker_index(inp, 4))

# part 2
print(find_marker_index(inp, 14))

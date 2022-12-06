#!/usr/bin/env python3

import sys
from pprint import pprint
from collections import defaultdict


inp = sys.stdin.readlines()[0].strip()


def find_marker_index(inp, n):
    buff = []
    for i, c in enumerate(inp):
        if i < n:
            buff.append(c)
        else:
            if len(set(buff)) == n:
                return i
            buff.pop(0)
            buff.append(c)
    return -1

# part 1
print(find_marker_index(inp, 4))

# part 2
print(find_marker_index(inp, 14))

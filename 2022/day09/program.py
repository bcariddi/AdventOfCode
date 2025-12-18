#!/usr/bin/env python3

import sys
from pprint import pprint
from collections import defaultdict


inp = [l.strip() for l in sys.stdin.readlines()]


# H and T start at the same initial position of (0, 0)
H_pos = [0, 0]
T_pos = [0, 0]



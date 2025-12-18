#!/usr/bin/env python3

import sys
from pprint import pprint
from collections import defaultdict


inp = [l.strip() for l in sys.stdin.readlines()]


# part 1
directories = defaultdict(list)
i = 0
while i < len(inp):
    if inp[i].split()[0] == '$': # line is instruction
        if inp[i].split()[1] == 'ls': # next lines are the files and dirs contained by current directory
            pass
        else: # changes which directory is current directory 
            pass

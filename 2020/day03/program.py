#!/usr/bin/env python3 

import sys

def get_trees(right, down=1):
    length = len(text[0]) - 1 # length of any line in the input
    i = 0 # keeps track of position on line
    trees = 0 # number of trees encountered

    for line in text:
        if i % down != 0:
            i += 1
            continue

        pos = i % length
        if line[pos] == '#':
            trees += 1

        i += right

    return trees

text = sys.stdin.readlines()

print(get_trees(1,1) * get_trees(3,1) * get_trees(5,1) * get_trees(7,1) * get_trees(1,2))

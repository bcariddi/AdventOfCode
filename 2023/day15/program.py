#!/usr/bin/env python3

import sys
import re
from pprint import pprint
from collections import defaultdict


inp = sys.stdin.read().strip()


def get_hash(string):
    curr = 0
    for char in string:
        curr += ord(char)
        curr *= 17
        curr %= 256
    return curr

# Part 1
steps = inp.split(',')
summ = 0
for step in steps:
    summ += get_hash(step)
print('Part 1:')
print(summ)

boxes = defaultdict(list)

for step in steps:
    label, number = re.split(r'-|=', step)
    lens = get_hash(label)

    if number:
        # Do add action
        exists = False
        target_prefix = f'[{label} '
        for i, item in enumerate(boxes[lens]):
            if item.startswith(target_prefix):
                exists = True
                boxes[lens][i] = f'[{label} {number}]'
                break
        
        if not exists:
            boxes[lens].append(f'[{label} {number}]')
    else:
        target_prefix = f'[{label} '
        for item in boxes[lens]:
            if item.startswith(target_prefix):
                boxes[lens].remove(item)
                break
    

# Calculate total power
total = 0
for box in boxes: 
    n = box + 1
    for i, lens in enumerate(boxes[box]):
        power = 0
        slot = i + 1
        length = int(lens[-2])
        power = n * slot * length
        total += power

print('Part 2:')
print(total)


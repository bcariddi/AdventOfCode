#!/usr/bin/env python3

import sys
from collections import defaultdict 

# Constants

TARGET = 'shiny gold'

held_by = defaultdict(set)
holds = defaultdict(list)

# Functions

def find_kind(kind):
    for bag in held_by[kind]:
        has_target.add(bag)
        find_kind(bag)

def find_count(kind):
    count = 0
    for num, bag in holds[kind]:
        count += num
        count += num * find_count(bag)
    return count

# Main

for line in sys.stdin:
    front, back = line.strip().split('contain')
    name = front.replace('bags','').strip()

    contents = []
    back = back.split(',')
    for bag in back:
        if not 'no other' in bag:
            contents.append(bag.replace('bags','').replace('bag','').replace('.','').strip())

    for bag in contents:
        num, kind = int(bag[0]), bag[2:] # probably gonna need to use this num for Part 2
        holds[name].append((num, kind))
        held_by[kind].add(name)

# Part 1
has_target = set()
find_kind(TARGET)
print(len(has_target))

# Part 2
count = find_count(TARGET)
print(count)

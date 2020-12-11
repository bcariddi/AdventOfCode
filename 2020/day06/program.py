#!/usr/bin/env python3 

import sys
import re

text = sys.stdin.readlines()

count1 = 0
count2 = 0

curr = ''
groups = []
group = dict()
pop = 0
for line in text:
    if line != '\n':
        curr += line.strip()
        pop += 1

    else: # complete group is in curr
        for question in curr:
            if question in group:
                group[question] += 1
            else:
                group[question] = 1

        # Part 1
        length = len(group)
        count1 += length
        
        # Part 2
        for question in group:
            if group[question] == pop:
                count2 += 1

        curr = ''
        group = dict()
        pop = 0

print(count1)
print(count2)

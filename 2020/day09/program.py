#!/usr/bin/env python3

import sys

PRELENGTH = 25

def is_valid(nums, num):
    for x in nums:
        if num - x in nums:
            return True

    return False

nums = [int(x) for x in sys.stdin.readlines()]

# Part 1
'''
for i, num in enumerate(nums):
    if i >= PRELENGTH:
        if not is_valid(nums[i-PRELENGTH:i], num):
            print(num)
            sys.exit()
'''

# Part 2 - invalid number was 10884537
invalid_num = 10884537

for start in range(len(nums)):
    curr = start

    contig = []
    while sum(contig) < invalid_num and curr < len(nums):
        contig.append(nums[curr])
        curr += 1

    if sum(contig) == invalid_num:
        print(min(contig) + max(contig))
        sys.exit()

#!/usr/bin/env python3

import sys
import statistics
from pprint import pprint

input = sys.stdin.readlines()

OPENS = {'(': ')', '[': ']', '{': '}', '<': '>'}
PENALTY = {')': 3, ']': 57, '}': 1197, '>': 25137}
COMPLETION = {')': 1, ']': 2, '}': 3, '>': 4}

def corrupted(line):
    stack = []
    for char in line:
        if char in OPENS:
            stack.append(char)
        else:
            last = stack.pop()
            expected = OPENS[last]
            if char != expected:
                stack.append(last)
                return PENALTY[char], stack

    return 0, stack


def find_reverse_stack(stack):
    result = ''
    for char in reversed(stack):
        result += OPENS[char]

    return result


def find_completion_score(completion):
    total = 0
    for char in completion:
        total *= 5
        total += COMPLETION[char]
    return total
        

score = 0
completion_scores = []
for line in input:
    line = line.strip()
    corrupt, stack = corrupted(line)
    score += corrupt

    if not corrupt:
        completion = find_reverse_stack(stack)
        completion_scores.append(find_completion_score(completion))
        
print(score)

middle = statistics.median(completion_scores)
print(middle)
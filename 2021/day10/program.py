#!/usr/bin/env python3

import sys
import statistics
from pprint import pprint

input = sys.stdin.readlines()

OPENS = {'(': ')', '[': ']', '{': '}', '<': '>'}

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
                if char == ')':
                    return 3, stack
                elif char == ']':
                    return 57, stack
                elif char == '}':
                    return 1197, stack
                elif char == '>':
                    return 25137, stack
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
        if char == ')':
            total += 1
        elif char == ']':
            total += 2
        elif char == '}':
            total += 3
        elif char == '>':
            total += 4
    return total
        

score = 0
completion_scores = []
for line in input:
    stack = []
    corrupt, stack = corrupted(line)
    score += corrupt

    if not corrupt:
        completion = find_reverse_stack(stack)
        completion_scores.append(find_completion_score(completion))
        
print(score)

middle = statistics.median(completion_scores)
print(middle)
#!/usr/bin/env python3

import sys

text = [x.strip() for x in sys.stdin.readlines()]

# Part 1

seen = set() # stores the index of instructions that have already ran
acc  = 0 # value of accumulator
i    = 0
curr = 0
while curr not in seen:
    i += 1
    seen.add(curr)

    op, arg = text[curr].split()
    #print(i, op, arg)
    arg = int(arg)

    if op == 'acc':
        acc += arg
        curr += 1
    elif op == 'jmp':
        curr += arg
    else:
        curr += 1

print(acc)

# Part 2 - brute forced

for to_change in range(len(text)):
    seen = set()
    acc  = 0
    i    = 0
    curr = 0

    while curr not in seen:
        i += 1
        seen.add(curr)

        op, arg = text[curr].split()
        arg = int(arg)

        if op == 'acc':
            acc += arg
            curr += 1
        elif op == 'jmp':
            if curr == to_change: # switch one jmp to nop
                curr += 1
            else:
                curr += arg
        else:
            if curr == to_change: # or switch one nop to jmp (or don't switch if we have a acc)
                curr += arg
            else:
                curr += 1

        if curr == len(text):
            print(acc)
            sys.exit()

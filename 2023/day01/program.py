#!/usr/bin/env python3

import sys
from pprint import pprint
from collections import defaultdict


DIGITS = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
}

inp = [l.strip() for l in sys.stdin.readlines()]


# part 1
'''
summ = 0
for line in inp:
    cal = ''
    for c in line:
        if c.isnumeric():
            cal += c
            break
    for c in reversed(line):
        if c.isnumeric():
            cal += c
            break
    summ += int(cal)

print(summ)
'''

# part 2
summ = 0
for line in inp:
    print(line)
    first_word_index = float('inf')
    first_word = ''
    last_word_index = 0
    last_word = ''

    for digit in DIGITS:
        floc = line.find(digit)
        if -1 < floc < first_word_index:
            first_word_index = floc
            first_word = digit

        rloc = line.rfind(digit)
        if rloc > last_word_index:
            last_word_index = rloc
            last_word = digit

    if first_word:
        line = line[:first_word_index] + DIGITS[first_word] + line[first_word_index:]
        if last_word:
            last_word_index += len(DIGITS[first_word])
        # line = line.replace(first_word, DIGITS[first_word], 1)
    if last_word:
        line = line[:last_word_index] + DIGITS[last_word] + line[last_word_index:]
        # line = DIGITS[last_word].join(line.rsplit(last_word, 1))

    print(line)
    cal = ''
    for c in line:
        if c.isnumeric():
            cal += c
            break
    for c in reversed(line):
        if c.isnumeric():
            cal += c
            break
    print(cal)
    print('-----')
    summ += int(cal)

print(summ)

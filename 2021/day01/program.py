#!/usr/bin/env python3

import sys

numbers = []

for line in sys.stdin:
    numbers.append(int(line))

# part 1

print(sum(y > x for x, y in zip(numbers, numbers[1:])))

# part 2

print(sum(y > x for x, y in zip(numbers, numbers[3:])))

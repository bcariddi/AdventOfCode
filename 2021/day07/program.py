#!/usr/bin/env python3

import sys
import statistics
from pprint import pprint

input = sys.stdin.readlines()

positions = [int(x) for x in input[0].split(',')]

# part 1

median = int(statistics.median(positions))

tot_diff = sum(abs(p - median) for p in positions)

print(tot_diff)

# part 2

mean = round(statistics.mean(positions))

def compute_fuel(n):
    return sum(abs(p - n) * (abs(p - n) + 1) // 2 for p in positions)

fuel = compute_fuel(mean)

if compute_fuel(mean - 1) < fuel:
    direction = -1
else:
    direction = 1

while compute_fuel(mean + direction) < fuel:
    mean += direction
    fuel = compute_fuel(mean)

print(fuel)
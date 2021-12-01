#!/usr/bin/env python3

import sys

numbers = []

for line in sys.stdin:
    numbers.append(int(line))

# part one

count = 0

for prev, curr in zip(numbers, numbers[1:]):
    if curr > prev:
        count += 1

print(count)

# part two

i = 0
count2 = 0

while i < len(numbers) - 3:
    sum1 = numbers[i] + numbers[i+1] + numbers[i+2]
    sum2 = numbers[i+1] + numbers[i+2] + numbers[i+3] 
    if sum2 > sum1:
        count2 +=1 
    
    i += 1

print(count2)
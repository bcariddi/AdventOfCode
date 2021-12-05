#!/usr/bin/env python3

import sys
import pprint
from collections import defaultdict

binaries = []

for line in sys.stdin:
    binaries.append(line.strip())

# part 1
verts = []

for i in range(len(binaries[0])):
    vert = [binaries[x][i] for x in range(len(binaries))]
    verts.append(vert)

gamma = ''
epsilon = ''
for vert in verts:
    gamma += max(set(vert), key=vert.count)
    epsilon += min(set(vert), key=vert.count)

power = int(gamma, 2) * int(epsilon, 2)
print(power)

# part 2
# oxygen
filtered_oxy = binaries.copy()

i = 0
count = 0
while len(filtered_oxy) > 1:
    index = i % len(filtered_oxy[0])
    vert = [filtered_oxy[x][index] for x in range(len(filtered_oxy))]
    zero_count = vert.count('0')
    one_count = vert.count('1')

    if one_count >= zero_count:
        filtered_oxy = list(filter(lambda x: x[index] == '1', filtered_oxy))
    else:
        filtered_oxy = list(filter(lambda x: x[index] == '0', filtered_oxy))

    i += 1
    count += 1

# co2
filtered_co2 = binaries.copy()

i = 0
count = 0
while len(filtered_co2) > 1:
    index = i % len(filtered_co2[0])
    vert = [filtered_co2[x][index] for x in range(len(filtered_co2))]
    zero_count = vert.count('0')
    one_count = vert.count('1')

    #print(filtered_co2)
    #print(f'index: {index}')
    #print(zero_count, one_count)

    if zero_count <= one_count:
        filtered_co2 = list(filter(lambda x: x[index] == '0', filtered_co2))
    else:
        filtered_co2 = list(filter(lambda x: x[index] == '1', filtered_co2))

    #print(filtered_co2)
    #print()

    i += 1
    count += 1

print(int(filtered_oxy[0], 2) * int(filtered_co2[0], 2))
#!/usr/bin/env python3

import sys

text = sys.stdin.readlines()

# Part 1
my_time = int(text[0])
bus_raw = text[1].split(',')
buses = []
for bus in bus_raw:
    if bus.isnumeric():
        buses.append(int(bus))

wait_times = []
for bus in buses:
    time_before = my_time % bus
    wait_times.append(bus - time_before)

wait = min(wait_times)
ID = buses[wait_times.index(wait)]

print(wait * ID)
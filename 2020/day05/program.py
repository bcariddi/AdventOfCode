#!/usr/bin/env python3

import sys

def get_row(rowdata, lowbound=0, upbound=127):
    if len(rowdata) == 1:
        if rowdata[0] == 'F':
            return lowbound
        else:
            return upbound

    mid = (upbound + lowbound) // 2

    if rowdata[0] == 'F':
        return get_row(rowdata[1:], lowbound, mid)
    else:
        return get_row(rowdata[1:], mid + 1, upbound)

def get_col(coldata, lowbound=0, upbound=7):
    if len(coldata) == 1:
        if coldata[0] == 'L':
            return lowbound
        else:
            return upbound

    mid = (upbound + lowbound) // 2

    if coldata[0] == 'L':
        return get_col(coldata[1:], lowbound, mid)
    else:
        return get_col(coldata[1:], mid + 1, upbound)

IDs = []
maxID = 0
for line in sys.stdin:
    rowdata, coldata = line[:-4], line[-4:]
    row, col = get_row(rowdata), get_col(coldata)

    ID = row * 8 + col
    IDs.append(ID)
    if ID > maxID:
        maxID = ID

# Part 1 solution
print(maxID)

IDs.sort()
low, high = IDs[0], IDs[-1]

for seat in range(low, high + 1):
    if seat not in IDs:
        # Part 2 solution
        print(seat)

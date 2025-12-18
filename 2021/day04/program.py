#!/usr/bin/env python3

import sys
import pandas as pd
from pprint import pprint

input = sys.stdin.read().split('\n\n')

numbers = [int(x) for x in input[0].split(',')]

board_strings = input[1:]

dfs = []
for board_string in board_strings:
    board_list = [[int(y) for y in row.split()] for row in board_string.split('\n')]
    df = pd.DataFrame(board_list)
    dfs.append(df)

x = dfs[1].shape[0]

# part 1 
'''
flag = True
for i, n in enumerate(numbers):
    if not flag:
        break

    dfs = [df.replace(n, -1) for df in dfs]

    for c, df in enumerate(dfs):
        for j in range(x):
            if list(df.iloc[:, j]) == [-1 for _ in range(x)] or list(df.iloc[j, :]) == [-1 for _ in range(x)]:
                flag = False
                summation = df.to_numpy().sum() + df.eq(-1).sum().sum()
                print(summation * n)
'''

# part 2

for i, n in enumerate(numbers):
    dfs = [df.replace(n, -1) for df in dfs]

    c = 0
    while c < len(dfs):
        df = dfs[c]

        removed = False
        for j in range(x):
            if list(df.iloc[:, j]) == [-1 for _ in range(x)] or list(df.iloc[j, :]) == [-1 for _ in range(x)]:
                if len(dfs) != 1:
                    del dfs[c]
                    removed = True
                else:
                    summation = df.to_numpy().sum() + df.eq(-1).sum().sum()
                    print(n * summation)
                    sys.exit()
                break
        
        if not removed:
            c += 1

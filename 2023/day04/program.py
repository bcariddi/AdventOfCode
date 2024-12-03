#!/usr/bin/env python3

import sys
from pprint import pprint
from collections import defaultdict


inp = [l.strip() for l in sys.stdin.readlines()]


def calc_score(x):
    return 2 ** (x - 1) if x != 0 else 0


def process_card(start_i, n):
    print(f'Card {start_i}: {n}')
    if n == 0:
        return 0

    for x in range(1 + start_i, 1 + start_i + n):
        print(x)
        if start_i + x >= len(MATCHES):
            return 1
        return 1 + process_card(start_i + x, MATCHES[start_i + x])


# total = 0
MATCHES = []
for i, card in enumerate(inp):
    half1, half2 = card.split('|')
    _, half1 = half1.split(':')

    w_nums = [int(x) for x in half1.split(' ') if x.isnumeric()]
    my_nums = [int(x) for x in half2.split(' ') if x.isnumeric()]

    # total += calc_score(len(set(w_nums) & set(my_nums)))
    
    n_match = len(set(w_nums) & set(my_nums))
    MATCHES.append(n_match)

print(MATCHES)

n_scorecards = 0
print(process_card(0, MATCHES[0]))

sys.exit()

for i, card in enumerate(MATCHES):
    print(f'Processing card {i}')
    n_scorecards += process_card(i, card)

print(n_scorecards)

# print(total)


#!/usr/bin/env python3

import sys
from pprint import pprint
from collections import defaultdict

MAX_RED   = 12
MAX_GREEN = 13
MAX_BLUE  = 14

inp = [l.strip() for l in sys.stdin.readlines()]


# part 1 and 2
summ = 0
for i, game in enumerate(inp):
    rounds = game.split(';')
    # game_valid = True
    maxrc, maxgc, maxbc = 0, 0, 0
    for r in rounds:
        ri, gi, bi = r.find('red'), r.find('green'), r.find('blue')

        if ri >= 0:
            rci = r.rfind(' ', 0, ri - 1)
            rc = int(r[rci:ri])
            maxrc = max(maxrc, rc)
            '''
            if rc > MAX_RED:
                game_valid = False
                break
            '''
        
        if gi >= 0:
            gci = r.rfind(' ', 0, gi - 1)
            gc = int(r[gci:gi])
            maxgc = max(maxgc, gc)
            '''
            if gc > MAX_GREEN:
                game_valid = False
                break
            '''

        if bi >= 0:
            bci = r.rfind(' ', 0, bi - 1)
            bc = int(r[bci:bi])
            maxbc = max(maxbc, bc)
            '''
            if bc > MAX_BLUE:
                game_valid = False
                break
            '''

        '''
        if not game_valid:
            break
        '''

    '''
    if game_valid:
        summ += i + 1
    '''

    summ += maxrc * maxgc * maxbc

print(summ)


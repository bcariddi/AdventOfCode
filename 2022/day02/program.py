#!/usr/bin/env python3

import sys


inp = [l.strip() for l in sys.stdin.readlines()]


OPP_ROC = 'A'
OPP_PAP = 'B'
OPP_SCI = 'C'

USR_ROC = 'X'
USR_PAP = 'Y'
USR_SCI = 'Z'


LOSS = 'X'
DRAW = 'Y'

def get_shape_value(shape):
    if shape == USR_ROC:
        return 1
    elif shape == USR_PAP:
        return 2
    else:
        return 3

def get_round_score(opp, usr):
    if opp == OPP_ROC and usr == USR_PAP or opp == OPP_PAP and usr == USR_SCI or opp == OPP_SCI and usr == USR_ROC:
        return 6
    elif opp == OPP_ROC and usr == USR_ROC or opp == OPP_PAP and usr == USR_PAP or opp == OPP_SCI and usr == USR_SCI:
        return 3
    return 0

# part 1
score = 0
for line in inp:
    opp, usr = line.split()
    score += get_shape_value(usr)
    score += get_round_score(opp, usr)
print(score)

# part 2
def get_score_from_res(opp, result):
    if result == LOSS:
        if opp == OPP_ROC:
            return get_shape_value(USR_SCI)
        elif opp == OPP_PAP:
            return get_shape_value(USR_ROC)
        return get_shape_value(USR_PAP)
    elif result == DRAW:
        if opp == OPP_ROC:
            return get_shape_value(USR_ROC) + 3
        elif opp == OPP_PAP:
            return get_shape_value(USR_PAP) + 3
        return get_shape_value(USR_SCI) + 3
    else:
        if opp == OPP_ROC:
            return get_shape_value(USR_PAP) + 6
        elif opp == OPP_PAP:
            return get_shape_value(USR_SCI) + 6
        return get_shape_value(USR_ROC) + 6

score2 = 0
for line in inp:
    opp, result = line.split()
    score2 += get_score_from_res(opp, result)
print(score2)

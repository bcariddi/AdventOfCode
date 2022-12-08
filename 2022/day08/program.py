#!/usr/bin/env python3

import sys
from pprint import pprint
from collections import defaultdict


trees = [[int(x) for x in l.strip()] for l in sys.stdin.readlines()]


def check_left(i, j):
    for a in range(0, j):
        if trees[i][a] >= trees[i][j]:
            return 0
    return 1

def check_right(i, j):
    for a in range(j + 1, width):
        if trees[i][a] >= trees[i][j]:
            return 0
    return 1

def check_up(i, j):
    for a in range(0, i):
        if trees[a][j] >= trees[i][j]:
            return 0
    return 1

def check_down(i, j):
    for a in range(i + 1, height):
        if trees[a][j] >= trees[i][j]:
            return 0
    return 1


def score_left(i, j):
    score = 1
    for a in reversed(range(1, j)):
        if trees[i][a] >= trees[i][j]:
            return score
        score += 1
    return score

def score_right(i, j):
    score = 1
    for a in range(j + 1, width - 1):
        if trees[i][a] >= trees[i][j]:
            return score
        score += 1
    return score

def score_up(i, j):
    score = 1
    for a in reversed(range(1, i)):
        if trees[a][j] >= trees[i][j]:
            return score
        score += 1
    return score

def score_down(i, j):
    score = 1
    for a in range(i + 1, height - 1):
        if trees[a][j] >= trees[i][j]:
            return score
        score += 1
    return score


height = len(trees)
width  = len(trees[0])
count  = 0
maxscore = 0
for i in range(height):
    for j in range(width):
        if i == 0 or j == 0 or i == height - 1 or j == width - 1:
            count += 1
        else:
            if check_left(i, j) or check_right(i, j) or check_up(i, j) or check_down(i, j):
                count += 1
            score = score_left(i, j) * score_right(i, j) * score_up(i, j) * score_down(i, j)
            maxscore = max(maxscore, score)
print(count)
print(maxscore)

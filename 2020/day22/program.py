#!/usr/bin/env python3

import sys


def compute_score(player):
    length = len(player)

    score = 0
    i = 0
    while i < length:
        score += (length - i) * player[i]
        i += 1

    return score


def main():
    text = sys.stdin.read().splitlines()
    spliti = text.index('')
    player1 = [int(x) for x in text[1:spliti]]
    player2 = [int(x) for x in text[spliti+2:]]

    while player1 and player2:
        p1, p2 = player1.pop(0), player2.pop(0)
        if p1 > p2:
            player1.append(p1)
            player1.append(p2)
        else:
            player2.append(p2)
            player2.append(p1)

    if player1:
        score = compute_score(player1)
    else:
        score = compute_score(player2)

    print(score)


if __name__ == '__main__':
    main()
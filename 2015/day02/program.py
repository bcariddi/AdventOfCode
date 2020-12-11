#!/usr/bin/env python3

import sys

paper = 0
ribbon = 0
for line in sys.stdin:
    l, w, h = map(int, line.split('x'))

    # wrapping paper
    area = 2*l*w + 2*w*h + 2*h*l
    minarea = min(l*w, w*h, h*l)

    giftpaper = area + minarea
    paper += giftpaper

    # ribbon
    vol = l*w*h
    minperim = min(2*l+2*w, 2*w+2*h, 2*h+2*l)

    giftribbon = vol + minperim
    ribbon += giftribbon

print(f'Wrapping paper: {paper}')
print(f'Ribbon: {ribbon}')

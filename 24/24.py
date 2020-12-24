#!/usr/bin/env python3

import collections
import fileinput
import re

MOVES = {
    "e": (2, 0),
    "w": (-2, 0),
    "se": (1, -1),
    "ne": (1, 1),
    "sw": (-1, -1),
    "nw": (-1, 1),
}


def find_tile(movestr):
    cursor = 0
    x = 0
    y = 0
    while cursor < len(movestr):
        move = movestr[cursor]
        if move in ("n", "s"):
            move = movestr[cursor:cursor+2]
            cursor += 2
        else:
            cursor += 1
        dx, dy = MOVES[move]
        x += dx
        y += dy
    return (x, y)



def part1():
    flips = [line.strip() for line in fileinput.input()]
    black = collections.defaultdict(bool)
    for flip in flips:
        tile = find_tile(flip)
        black[tile] = not black[tile]
    return sum(v for v in black.values())

def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
#print(part2())
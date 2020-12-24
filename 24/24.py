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
    return count_black_dict(black)


def get_neighbors(x, y):
    return [(x + dx, y + dy) for dx, dy in MOVES.values()]

def count_black_dict(black):
    return sum(v for v in black.values())

def count_black(iter, black):
    return sum(black[coords] for coords in iter)

def do_turn(x, y, black, new_black):
    if (x, y) in new_black:
        return
    neighbors = get_neighbors(x, y)
    black_neighbors = count_black(neighbors, black)
    new_black[(x, y)] = (black_neighbors == 2 or (black[(x, y)] and black_neighbors == 1))
    if black[(x, y)]:
        for x_, y_ in neighbors:
            do_turn(x_, y_, black, new_black)


def next_turn(black):
    new_black = collections.defaultdict(bool)
    for x, y in list(black.keys()):
        do_turn(x, y, black, new_black)
    return new_black


def part2():
    flips = [line.strip() for line in fileinput.input()]
    black = collections.defaultdict(bool)
    for flip in flips:
        tile = find_tile(flip)
        black[tile] = not black[tile]
    for _ in range(100):
        black = next_turn(black)
    return count_black_dict(black)

#print(part1())
print(part2())
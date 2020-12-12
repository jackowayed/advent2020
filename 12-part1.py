#!/usr/bin/env python3

import fileinput
import re


def rotate(dir, deg, dy, dx):
    HEADINGS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    start_idx = HEADINGS.index((dy, dx))
    rotations = deg // 90
    if dir == "L":
        rotations *= -1
    return HEADINGS[(start_idx + rotations) % len(HEADINGS)]


def dead_code():
    if deg == 180:
        dy = -dy
        dx = -dx
    elif deg == 270:
        dir = "R" if dir == "L" else "L"
        return rotate(dir, 90, dy, dx)
    assert deg == 90


def part1():
    dy = 0
    dx = 1
    x = 0
    y = 0
    for line in fileinput.input():
        dir = line[0]
        val = int(line[1:])
        if dir == "N":
            y += val
        elif dir == "S":
            y -= val
        elif dir == "E":
            x += val
        elif dir == "W":
            x -= val
        elif dir == "F":
            x += dx * val
            y += dy * val
        else:
            assert dir in ("L", "R")
            dy, dx = rotate(dir, val, dy, dx)
    return abs(x) + abs(y)

def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
#print(part2())
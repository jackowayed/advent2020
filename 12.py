#!/usr/bin/env python3

import fileinput
import re

def sign(n):
    if n < 0:
        return -1
    if n > 0:
        return 1
    return 0


def rotate(dir, deg, dy, dx):
    if deg == 180:
        return (-dy, -dx)
    if deg == 270 and dir == "R" or deg == 90 and dir == "L":
        return (dx, -dy)
    else:
        assert deg == 90 and dir == "R" or deg == 270 and dir == "L"
        return (-dx, dy)



def part2():
    dy = 1
    dx = 10
    x = 0
    y = 0
    for line in fileinput.input():
        dir = line[0]
        val = int(line[1:])
        if dir == "N":
            dy += val
        elif dir == "S":
            dy -= val
        elif dir == "E":
            dx += val
        elif dir == "W":
            dx -= val
        elif dir == "F":
            x += dx * val
            y += dy * val
        else:
            assert dir in ("L", "R")
            dy, dx = rotate(dir, val, dy, dx)
    return abs(x) + abs(y)

print(part2())
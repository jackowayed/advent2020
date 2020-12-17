#!/usr/bin/env python3

import collections
import fileinput
import re

Coordinate = collections.namedtuple("Coordinate", ["x", "y", "z", "a"])

def neighbors(c, m):
    ct = 0
    x, y, z, a = c
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for da in range(-1, 2):
                    if dx == 0 and dy == 0 and dz == 0 == da:
                        continue
                    ct += (x + dx, y + dy, z + dz, a + da) in m
    return ct


def do_turn(m):
    new_m = set()
    candidates = set()
    for x,y,z,a in m:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    for da in range(-1, 2):
                        candidates.add(Coordinate(
                            x + dx, y + dy, z + dz, a + da))
    for c in candidates:
        n = neighbors(c, m)
        if n == 3 or (n == 2 and c in m):
            new_m.add(c)
    return new_m


def part1():
    m = set()
    start_map = [line.strip() for line in fileinput.input()]
    for y, line in enumerate(start_map):
        for x, char in enumerate(line):
            if char == "#":
                m.add(Coordinate(x, y, 0, 0))
            else:
                assert char == "."
    
    for _ in range(6):
        m = do_turn(m)
    return len(m)

def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
#print(part2())
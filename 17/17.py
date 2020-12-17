#!/usr/bin/env python3

import collections
import fileinput
import re

class Coordinate__:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, c):
        return Coordinate__(c.x + self.x, 
            c.y + self.y,
            c.z + self.z)

Coordinate = collections.namedtuple("Coordinate", ["x", "y", "z"])

def neighbors(c, m):
    ct = 0
    x, y, z = c
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if dx == 0 and dy == 0 and dz == 0:
                    continue
                ct += (x + dx, y + dy, z + dz) in m
    return ct


def do_turn(m):
    new_m = set()
    candidates = set()
    for x,y,z in m:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    candidates.add(Coordinate(
                        x + dx, y + dy, z + dz))
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
                m.add(Coordinate(x, y, 0))
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
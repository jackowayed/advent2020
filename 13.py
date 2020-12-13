#!/usr/bin/env python3

import fileinput
import re


def part1():
    lines = [line.strip() for line in fileinput.input()]
    start_time = int(lines[0])
    buses = [int(l) for l in lines[1].split(",") if not l.startswith("x")]
    min_ = 100000
    min_freq = None
    for freq in buses:
        wait = (freq - (start_time % freq)) % freq
        if wait < min_:
            min_ = wait
            min_freq = freq
    return min_freq * min_

def safe_int(s):
    if s == "x":
        return None
    return int(s)

def evaluate(buses, t):
    assert t % buses[0] == 0
    for b in buses:
        if b is None:
            pass
        elif t % b != 0:
            return False
        t += 1
    return True


def part2():
    lines = [line.strip() for line in fileinput.input()]
    buses = [safe_int(l) for l in lines[1].split(",")]
    t = 100000000000000
    while t % buses[0] != 0:
        t += 1
    while True:
        if evaluate(buses, t):
            return t
        t += buses[0]

    print(buses)
    return

#print(part1())
print(part2())
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

def brute_euclid(y, n):
    for z in range(n):
        if (z * y) % n == 1:
            return z
    assert False

# https://brilliant.org/wiki/chinese-remainder-theorem/
def solve(buses):
    mods = []
    for i, val in enumerate(buses):
        if val:
            mods.append((i, val))
    big_n = 1
    for _, mod in mods:
        big_n *= mod
    x = 0
    for a_i, mod in mods:
        y_i = big_n // mod
        z_i = brute_euclid(y_i, mod)
        x += a_i * y_i * z_i
    return x
    

def part2():
    lines = [line.strip() for line in fileinput.input()]
    buses = [safe_int(l) for l in lines[1].split(",")]
    return solve(buses)

#print(part1())
print(part2())
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

def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
#print(part2())
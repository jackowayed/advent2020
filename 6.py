#!/usr/bin/env python3

import fileinput


def part1():
    sum = 0
    seen = set()
    for line in fileinput.input():
        if line.strip():
            for c in line.strip():
                seen.add(c)
        else:
            sum += len(seen)
            seen.clear()
    if seen:
        sum += len(seen)
    return sum

def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
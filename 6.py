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
    sum = 0
    has_started = False
    valid = set()
    for line in fileinput.input():
        if line.strip():
            if not has_started:
                has_started = True
                valid = set(line.strip())
            else:
                valid &= set(line.strip())
        else:
            sum += len(valid)
            has_started = False
    if valid and has_started:
        sum += len(valid)
    return sum


print(part2())
#!/usr/bin/env python3

import fileinput

def seat_id(line):
    binary = line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    return int(binary, 2)


def part2():
    ids = sorted([seat_id(line.strip()) for line in fileinput.input()])
    for i in range(len(ids) - 1):
        if ids[i + 1] - ids[i] == 2:
            print(ids[i] + 1)

def part1():
    print(max(seat_id(line.strip()) for line in fileinput.input()))

part2()

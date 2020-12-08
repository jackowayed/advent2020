#!/usr/bin/env python3

import fileinput
import re

def parse_line(line):
    tokens = line.split(" ")
    ins = tokens[0]
    val = int(tokens[1])
    return ins, val

def part1():
    instructions = [line.strip() for line in fileinput.input()]
    acc = 0
    idx = 0
    seen_idx = set()
    while idx not in seen_idx:
        seen_idx.add(idx)
        ins, val = parse_line(instructions[idx])
        if ins == "acc":
            acc += val
            idx += 1
        elif ins == "jmp":
            idx += val
        else:
            assert ins == "nop"
            idx += 1
    return acc

def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
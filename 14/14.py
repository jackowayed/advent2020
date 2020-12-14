#!/usr/bin/env python3

import collections
import fileinput
import re

def ormask(mask_str):
    assert len(mask_str) == 36
    mask = mask_str.replace("X", "0")
    return int(mask, 2)

def andmask(mask_str):
    assert len(mask_str) == 36
    mask = mask_str.replace("X", "1")
    return int(mask, 2)

def part1():
    mem = collections.defaultdict(int)
    or_mask = None
    and_mask = None
    for line in fileinput.input():
        if line.startswith("mask"):
            mask_str = line.strip()[7:]
            or_mask = ormask(mask_str)
            and_mask = andmask(mask_str)
        else:
            assert line.startswith("mem")
            g = re.match(r"^mem\[(\d+)\] = (\d+)$", line)
            addr, val = g.groups()
            mem[addr] = int(val) & and_mask | or_mask
    return sum(mem.values())

def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
#print(part2())
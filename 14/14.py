#!/usr/bin/env python3

import collections
import fileinput
import re

def ormask(mask_str):
    assert len(mask_str) == 36
    mask = mask_str.replace("X", "0")
    return int(mask, 2)

def masks_(mask_str):
    starter = ormask(mask_str)
    additions = [0]
    for place in range(len(mask_str)):
        if mask_str[-(place+1)] == "X":
            val = 2 ** (place)
            new_additions = []
            for add in additions:
                new_additions.append(add)
                new_additions.append(add + val)
            additions = new_additions
    return additions

def part2():
    mem = collections.defaultdict(int)
    or_mask = None
    for line in fileinput.input():
        if line.startswith("mask"):
            mask_str = line.strip()[7:]
            or_mask = ormask(mask_str)
            and_masks = masks_(mask_str)
            #print([bin(m) for m in masks])
        else:
            assert line.startswith("mem")
            g = re.match(r"^mem\[(\d+)\] = (\d+)$", line)
            addr, val = g.groups()
            for mask in and_masks:
                mem[int(addr) | or_mask & mask] = int(val)
    print(mem)
    return sum(mem.values())

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

#print(part1())
print(part2())
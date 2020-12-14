#!/usr/bin/env python3

import collections
import fileinput
import re

def ormask(mask_str):
    assert len(mask_str) == 36
    mask = mask_str.replace("X", "0")
    return int(mask, 2)

def do_mask(v, mask_str):
    v |= ormask(mask_str)
    print("start")
    # (or_mask, and_mask)
    masks = [(0, 2**35)]
    for place in range(len(mask_str)):
        if mask_str[-(place+1)] == "X":
            mask = 2 ** (place)
            new_masks = []
            for or_mask, and_mask in masks:
                # turn the bit on
                new_masks.append((or_mask + mask, and_mask))
                # turn the bit off
                new_masks.append((or_mask, and_mask - mask))
            print((masks, new_masks, mask))
            masks = new_masks
    return [v | or_mask & and_mask for or_mask, and_mask in masks]

def part2():
    mem = collections.defaultdict(int)
    mask_str = None
    for line in fileinput.input():
        if line.startswith("mask"):
            mask_str = line.strip()[7:]
            #print([bin(m) for m in masks])
        else:
            assert line.startswith("mem")
            g = re.match(r"^mem\[(\d+)\] = (\d+)$", line)
            addr_s, val = g.groups()
            for addr in do_mask(int(addr_s), mask_str):
                mem[addr] = int(val)
    for k, v in sorted(mem.items()):
        print((bin(k), v))
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
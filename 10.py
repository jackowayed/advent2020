#!/usr/bin/env python3

import fileinput
import re

def jumps(nums, n):
    return sum(nums[i] + n in nums for i in range(len(nums) - 1))


def read():
    raw = sorted([int(line.strip()) for line in fileinput.input()])
    nums = [0]
    nums.extend(raw)
    nums.append(nums[-1] + 3)
    return nums

def part1():
    nums = read()
    voltage = 0
    one_jumps = 0
    three_jumps = 0
    while voltage < nums[-1]:
        if (voltage + 1) in nums:
            one_jumps += 1
            voltage += 1
        elif (voltage + 3) in nums:
            three_jumps += 1
            voltage += 3
    return one_jumps * three_jumps

mem = dict()

def arrangements(nums, after_idx):
    if after_idx in mem:
        return mem[after_idx]
    r = arrangements_logic(nums, after_idx)
    mem[after_idx] = r
    return r

def arrangements_logic(nums, after_idx):
    if after_idx == len(nums) - 1:
        return 1
    sum = 0
    for idx in range(after_idx + 1, after_idx + 4):
        if idx < len(nums):
            pass#print(nums[idx] - nums[after_idx])
        if idx < len(nums) and ((nums[idx] - nums[after_idx]) in (1,3)):
            print(f"made it {(nums[after_idx], nums[idx])}")
            sum += arrangements_logic(nums, idx)
    return sum

    


def part2():
    nums = read()
    return arrangements(nums, 0)

#print(part1())
print(part2())
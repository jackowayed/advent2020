#!/usr/bin/env python3

import fileinput
import re

WINDOW_SIZE = 25

def check(i, nums):
    for x in range(WINDOW_SIZE):
        for y in range(WINDOW_SIZE):
            if nums[i-x-1] + nums[i-y-1] == nums[i]:
                return True
    return False

def part1():
    nums = [int(line.strip()) for line in fileinput.input()]
    for i in range(WINDOW_SIZE, len(nums)):
        if not check(i, nums):
            return nums[i]

def part2():
    nums = [int(line.strip()) for line in fileinput.input()]
    for start in range(len(nums)):
        for stop in range(len(nums)):
            if start < stop and sum(nums[start:stop+1]) == 1721308972: 
                return min(nums[start:stop+1]) + max(nums[start:stop+1])


print(part2())
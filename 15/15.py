#!/usr/bin/env python3

import collections
import fileinput
import re


def part1():
    input = "2,1,10,11,0,6"
    #input = "0,3,6"
    starts = [int(i) for i in input.split(",")]
    last = dict()
    turn = 1
    for s in starts:
        last[s] = turn
        turn += 1
    last_num = 0
    last_num_age = turn - last[0]
    last[last_num] = turn
    while turn < 30000000:
        turn += 1
        last_num = last_num_age
        if last_num in last:
            last_num_age = turn - last[last_num]
        else:
            last_num_age = 0
        last[last_num] = turn
    return last_num

def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
#print(part2())
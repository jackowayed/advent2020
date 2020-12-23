#!/usr/bin/env python3

import collections
import fileinput
import re

def rotate_to_front(l, val):
    while l[0] != val:
        l.insert(0, l.pop())

def part1():
    input = "962713854" #"389125467"
    cups = [int(i) for i in input]
    cups = solve(cups, 100)
    return "".join([str(i) for i in cups[1:]])

def solve(cups, turns):
    n_cups = len(cups)
    for turn in range(turns):
        if turn % 1000 == 0:
            print(turn)
        start = cups[0]
        pickup = cups[1:4]
        cups = cups[:1] + cups[4:]
        dest_idx = -1
        for n in range(cups[0] - 1, -1, -1):
            if n in cups:
                dest_idx = cups.index(n)
                break
        if dest_idx == -1:
            max_ = max(cups)
            dest_idx = cups.index(max_)
        old_cups = cups
        cups = cups[:dest_idx + 1] + pickup + cups[dest_idx + 1:]
        assert len(cups) == n_cups
        #    cups = old_cups[:len(cups) - n_cups] + cups
        #    print(cups)
        next_idx = (cups.index(start) + 1) % len(cups)
        rotate_to_front(cups, cups[next_idx])
    rotate_to_front(cups, 1)
    return cups

def part2():
    #input = "962713854" 
    input = "389125467"
    cups = [int(i) for i in input]
    cups.extend(range(len(input), 1000000))
    cups = solve(cups, 10000000)
    return cups[1] * cups[2]

print(part1())
#print(part2())
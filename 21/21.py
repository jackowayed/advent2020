#!/usr/bin/env python3

import collections
import fileinput
import re


def parse(line):
    m = re.fullmatch("(.*) \(contains (.*)\)", line)
    ingredients = set(m.group(1).split(" "))
    allergens = set(m.group(2).split(", "))
    return (ingredients, allergens)


def part1():
    w = [parse(line.strip()) for line in fileinput.input()]
    poss = dict()
    for ingredients, allergens in w:
        for a in allergens:
            if a in poss:
                poss[a] &= ingredients
            else:
                poss[a] = set(ingredients)
    print(poss)
    done = False
    while not done:
        done = True
        for a, i in poss.items():
            if len(i) == 1:
                for a_, i_ in poss.items():
                    if a_ != a and i < i_:
                        i_ -= i
                        done = False
    return ",".join([i.pop() for a, i in sorted(poss.items())])


def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
#print(part2())
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
    poss_i = set()
    for ingredients in poss.values():
        poss_i |= ingredients
    ct = 0
    for ingredients, _ in w:
        ct += sum(i not in poss_i for i in ingredients)
    return ct

def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
#print(part2())
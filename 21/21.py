#!/usr/bin/env python3

import collections
import fileinput
import re


def parse(line):
    m = re.fullmatch("(.*) \(contains (.*)\)", line)
    ingredients = m.group(1).split(" ")
    allergens = set(m.group(2).split(", "))
    return (ingredients, allergens)


def part1():
    w = [parse(line.strip()) for line in fileinput.input()]
    possible_allergens = dict()
    for ingredients, allergens in w:
        for i in ingredients:
            if i in possible_allergens:
                possible_allergens[i] &= allergens
            else:
                possible_allergens[i] = allergens
    print(possible_allergens)
    none = set()
    for i, allergens in possible_allergens.items():
        if not allergens:
            none.add(i)
    print(none)
    ct = 0
    for ingredients, _ in w:
        ct += sum(i in none for i in ingredients)
    return ct

def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
#print(part2())
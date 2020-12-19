#!/usr/bin/env python3

import collections
import fileinput
import re
import unittest

#Rule = collections.namedtuple("Rule", ["raw", "re"])
class Rule:
    def __init__(self, raw, re):
        self.raw = raw
        self.re = re

def make_rule(raw):
    idx = raw.find('"')
    if idx == -1:
        reg = None
    else:
        reg = raw[idx + 1]
    return Rule(raw.strip().split(" "), reg)

def resolve_rule(rules, rid):
    regex = ""
    for t in rules[rid].raw:
        addon = ""
        if t == "|":
            addon = "|"
        else:
            addon = f"({rules[t].re})"
        regex += addon
    return regex

def resolve_rules(rules):
    has_unresolved = True
    while has_unresolved:
        has_unresolved = False
        for rid in rules.keys():
            if rules[rid].re:
                continue
            if all(orid == "|" or rules[orid].re for orid in rules[rid].raw):
                rules[rid].re = resolve_rule(rules, rid)
                assert rules[rid].re, rid
            else:
                has_unresolved = True

def matches_zero(line, rules):
    return bool(re.fullmatch(rules["0"].re, line.strip()))

def part1():
    rules = dict()
    it = fileinput.input()
    for line in it:
        if not line.strip():
            break
        sp = line.split(":")
        rules[sp[0]] = make_rule(sp[1])
    resolve_rules(rules)
    print("resolved")
    return sum(matches_zero(line, rules) for line in it)

def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return


#print(Rule([], None))
#print(make_rule(" 43 13"))

print(part1())
#print(part2())

class Test(unittest.TestCase):
    pass

#unittest.main()
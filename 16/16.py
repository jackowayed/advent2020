#!/usr/bin/env python3

import collections
import fileinput
import re

def field_matches_rule(ticket, rule):
    for low, high in rule:
        if ticket >= low and ticket <= high:
            return True
    return False

def field_valid(f, rules):
    return any(field_matches_rule(f, rule) for rule in rules)

def ticket_valid(ticket, rules):
    return sum((0 if field_valid(f, rules.values()) else f)
         for f in ticket)


def parse_ticket(s):
    return list(map(int, s.split(",")))

def part1():
    field_ranges = dict()
    it = fileinput.input()
    for line_ in it:
        line = line_.strip()
        if not line:
            break
        fs = line.split(":")
        g = re.match(r"^ (\d+)-(\d+) or (\d+)-(\d+)$", fs[1])
        gs = g.groups()
        field_ranges[fs[0]] = [(int(gs[0]), int(gs[1])), 
            (int(gs[2]), int(gs[3]))]
    assert next(it).startswith("your ticket")
    my_ticket = parse_ticket(next(it))
    assert not next(it).strip()
    assert next(it).startswith("nearby tickets")
    nearby_tickets = [parse_ticket(line) for line in it if line.strip()]
    return sum(ticket_valid(ticket, field_ranges) for ticket in nearby_tickets)

def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
#print(part2())
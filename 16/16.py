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
    return all(field_valid(f, rules.values()) for f in ticket)




def do_ticket(ticket, rules, valids):
    for i, f in enumerate(ticket):
        for name, rule in rules.items():
            if not field_matches_rule(f, rule):
                valids[i].discard(name)



def parse_ticket(s):
    return list(map(int, s.split(",")))

def part2():
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
    valid_tickets = list(filter(lambda ticket: ticket_valid(ticket, field_ranges), nearby_tickets))
    valid_tickets.append(my_ticket)

    num_fields = len(valid_tickets[0])
    assert num_fields == len(field_ranges)
    valids = [set(field_ranges.keys()) for _ in range(num_fields)]
    for t in valid_tickets:
        do_ticket(t, field_ranges, valids)
    print(valids)





print(part2())
#print(part2())
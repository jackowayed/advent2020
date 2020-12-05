#!/usr/bin/env python3

# https://adventofcode.com/2020/day/4

import fileinput

REQUIRED_FIELDS = set(
    ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
ALLOWED_FIELDS = REQUIRED_FIELDS.copy()
ALLOWED_FIELDS.add("cid")


def valid(fields):
    assert fields <= ALLOWED_FIELDS
    return REQUIRED_FIELDS <= fields

def process_line(line, fields):
    tokens = line.split(" ")
    for t in tokens:
        field = t.split(":")[0]
        fields.add(field)

def main():
    n_valid = 0
    n_invalid = 0
    n_lines = 0

    seen_fields = set()
    for line in fileinput.input():
        n_lines += 1
        if line.strip():
            process_line(line, seen_fields)
        else:
            if valid(seen_fields):
                n_valid += 1
            else:
                n_invalid += 1
            seen_fields.clear()
    if seen_fields:
        if valid(seen_fields):
            n_valid += 1
        else:
           n_invalid += 1
    print(n_valid)
    print(n_invalid)


main()
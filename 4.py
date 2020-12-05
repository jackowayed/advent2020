#!/usr/bin/env python3

# https://adventofcode.com/2020/day/4

import fileinput
import re

REQUIRED_FIELDS = set(
    ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
ALLOWED_FIELDS = REQUIRED_FIELDS.copy()
ALLOWED_FIELDS.add("cid")


def valid(fields):
    assert fields <= ALLOWED_FIELDS
    return REQUIRED_FIELDS <= fields

def is_color(val):
    return re.match("^#[a-f0-9]{6}$", val)

def field_valid(name, val):
    if name == "byr":
        i = int(val)
        return i >= 1920 and i <= 2002
    elif name == "iyr":
        i = int(val)
        return i >= 2010 and i <= 2020
    elif name == "eyr":
        i = int(val)
        return i >= 2020 and i <= 2030
    elif name == "hgt":
        if len(val) < 2 or val[-2:] not in ("in", "cm"):
            return False
        num = int(val[:-2])
        if val[-2:] == "in":
            return num >= 59 and num <= 76
        return num >= 150 and num <= 193
    elif name == "hcl" or name == "ecl":
        return is_color(val)
    elif name == "pid":
        return re.match("^\d{9}$", val)
    elif name == "cid":
        return True
    else:
        assert False

def check_field(token, fields):
    field_name, value = token.split(":")
    if field_valid(field_name, value):
        fields.add(field_name)


def process_line(line, fields):
    tokens = line.split(" ")
    for t in tokens:
        check_field(t, fields)

def main():
    n_valid = 0
    n_invalid = 0
    n_lines = 0

    seen_fields = set()
    for line in fileinput.input():
        n_lines += 1
        if line.strip():
            process_line(line.strip(), seen_fields)
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
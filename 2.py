#!/usr/bin/env python3

import re
import fileinput

def is_valid(line):
    m = re.match("(\w+)-(\w+) ([a-z]): ([a-z]+)$", line)
    assert m
    minimum = int(m.group(1))
    maximum = int(m.group(2))
    char = m.group(3)
    password = m.group(4)

    occurrences = password.count(char)
    return occurrences >= minimum and occurrences <= maximum

def main():
    print(sum(is_valid(line.strip()) for line in fileinput.input()))

main()

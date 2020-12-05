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

    one = password[minimum - 1]
    two = password[maximum - 1]
    return (one == char and two != char) or (two == char and one != char)

def main():
    print(sum(is_valid(line.strip()) for line in fileinput.input()))

main()

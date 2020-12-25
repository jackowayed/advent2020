#!/usr/bin/env python3

import collections
import fileinput
import re

def do_turn(val, subject):
    val *= subject
    val = val % 20201227
    return val


def find_secret(pubkey, subject):
    val = 1
    for i in range(1000000000000):
        val = do_turn(val, subject)
        if val == pubkey:
            return i+1
    raise "whatever"


def part1():
    door = 15113849
    lock = 4206373
    #door = 5764801
    #lock = 17807724
    #return find_secret(5764801), find_secret(17807724)
    door_secret = find_secret(door, 7)
    val = 1
    for _ in range(door_secret):
        val = do_turn(val, lock)
    return val


def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
#print(part2())
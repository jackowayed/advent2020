#!/usr/bin/env python3

import collections
import fileinput
import re


def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

def read_deck(it):
    deck = collections.deque()
    for line in it:
        line = line.strip()
        if not line:
            break
        deck.append(int(line))
    return deck

def play(one, two):
    while one and two:
        one_c = one.popleft()
        two_c = two.popleft()
        if one_c > two_c:
            one.append(one_c)
            one.append(two_c)
        else:
            two.append(two_c)
            two.append(one_c)
    if one:
        return one
    else:
        return two


def score(deck):
    sc = 0
    mult = 1
    while deck:
        sc += deck.pop() * mult
        mult += 1
    return sc


def part1():
    it = fileinput.input()
    assert next(it) == "Player 1:\n"
    deck_one = read_deck(it)
    assert next(it) == "Player 2:\n"
    deck_two = read_deck(it)
    winner = play(deck_one, deck_two)
    return score(winner)

print(part1())
#print(part2())
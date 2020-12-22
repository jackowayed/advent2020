#!/usr/bin/env python3

import collections
import fileinput
import re



def hashable(dq):
    out =  ",".join(str(i) for i in dq)
    return out

def hashables(one, two):
    #print(f"{hashable(one)}|{hashable(two)}")
    return f"{hashable(one)}|{hashable(two)}"


def copy(dq, l):
    c = dq.copy()
    while len(c) > l:
        c.pop()
    return c

def play2(one, two):
    history = set()
    while one and two:
        if (hashables(one, two)) in history:
            print("the rule")
            return one, "one"
        history.add(hashables(one, two))
        one_c = one.popleft()
        two_c = two.popleft()
        winner = None
        if one_c <= len(one) and two_c <= len(two):
            deck, winner = play2(copy(one, one_c),
                copy(two, two_c))
        else:
            if one_c > two_c:
                winner = "one"
            else:
                winner = "two"
        if winner == "one":
            one.append(one_c)
            one.append(two_c)
        else:
            assert winner == "two", winner
            two.append(two_c)
            two.append(one_c)
        
    if one:
        return one, "one"
    else:
        return two, "two"



def part2():
    it = fileinput.input()
    assert next(it) == "Player 1:\n"
    deck_one = read_deck(it)
    assert next(it) == "Player 2:\n"
    deck_two = read_deck(it)
    winner, _ = play2(deck_one, deck_two)
    return score(winner)


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

#print(part1())
print(part2())
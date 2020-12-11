#!/usr/bin/env python3

import fileinput
import re

def get_map():
    return [[c for c in line.strip()] for line in fileinput.input()]

def get_adjacent(seats, x, y):
    ct = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx == len(seats) or ny == len(seats[0]):
                continue
            if seats[nx][ny] == "#":
                ct += 1
    return ct

def copy(seats):
    return [row.copy() for row in seats]


def apply_rules(old_seats):
    seats = copy(old_seats)
    for x in range(len(seats)):
        for y in range(len(seats[0])):
            if seats[x][y] == ".":
                continue
            ct = get_adjacent(old_seats, x, y)
            if ct == 0 and old_seats[x][y] == "L":
                seats[x][y] = "#"
            elif ct >= 4 and old_seats[x][y] == "#":
                seats[x][y] = "L"
    return seats


def part1():
    seats = get_map()
    while True:
        old_seats = seats
        seats = apply_rules(old_seats)
        if old_seats == seats:
            break
    ct = 0
    for x in range(len(seats)):
        for y in range(len(seats[0])):
            if seats[x][y] == "#":
                ct += 1
    return ct

def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
#print(part2())
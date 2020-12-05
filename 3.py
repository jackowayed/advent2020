#!/usr/bin/env python3

import fileinput

def read_file():
    return [line.strip() for line in fileinput.input()]

def part1():
    trees = 0
    x = 0
    for row in read_file():
        if row[x % len(row)] == "#":
            trees += 1
        x += 3
    print(trees)
    
def check_slope(dx, dy):
    trees = 0
    x = 0
    y = 0
    grid = [row for row in read_file()]
    while y < len(grid):
        if grid[y][x % len(grid[0])] == "#":
            trees += 1
        x += dx
        y += dy
    return trees

def part2():
    print(check_slope(1, 1) * check_slope(3, 1) 
        * check_slope(5, 1) * check_slope(7, 1)
        * check_slope(1, 2))


part2()
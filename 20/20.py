#!/usr/bin/env python3

import collections
import fileinput
import functools
import operator
import re

Tile = collections.namedtuple("Tile", ["id", "grid"])

def index(run, idx, ind):
    ind[run].append(idx)
    ind[run[::-1]].append(idx)

def index_tile(tile, ind):
    grid = tile.grid
    top = grid[0]
    bottom = grid[-1]
    left = "".join([l[0] for l in grid])
    right = "".join([l[-1] for l in grid])
    for run in (top, bottom, left, right):
        index(run, tile.id, ind)

def read_tile(it) -> Tile:
    header = next(it, None)
    if not header:
        return None
    g = re.search("\d+", header)
    id = int(g.group(0))
    grid = []
    for line in it:
        if not line.strip():
            break
        grid.append(line.strip())
    return Tile(id, grid)

def part1():
    it = fileinput.input()
    tile = read_tile(it)
    tiles = dict()
    borders = collections.defaultdict(list)
    while tile:
        tiles[tile.id] = tile
        index_tile(tile, borders)
        tile = read_tile(it)
    #print(tiles)

    edges = [ids[0] for ids in borders.values() if len(ids) == 1]
    counts = collections.defaultdict(int)
    corners = []
    for idx in edges:
        counts[idx] += 1
        if counts[idx] == 4:
            corners.append(idx)
    
    if False:#for tile in tiles.values():
        grid = tile.grid
        top = grid[0]
        bottom = grid[-1]
        left = "".join([l[0] for l in grid])
        right = "".join([l[-1] for l in grid])
        num_not_found = 0
        for run in (top, bottom, left, right):
            num_not_found += run not in borders
        assert num_not_found <= 2
        if num_not_found == 2:
            corners.append(tile.id)
        print(num_not_found)
    return functools.reduce(operator.mul, corners, 1)

def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

print(part1())
#print(part2())
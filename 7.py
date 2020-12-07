#!/usr/bin/env python3

import fileinput


def parse_rest(rest):
    if "no other bags" in rest:
        return []
    bagses = rest.split(", ")
    ret = []
    for one_bag in bagses:
        tokens = one_bag.split(" ")
        ret.append((" ".join(tokens[1:-1]), int(tokens[0])))
    return ret
    
    
def parse():
    graph = dict()
    for line in fileinput.input():
        idx = line.find("bags")
        start = line[:idx-1]
        graph[start] = parse_rest(line[idx + len("bags contain "):])
    return graph


def dfs(graph, start, search):
    if start == search:
        return True
    for next_bag, _ in graph[start]:
        if dfs(graph, next_bag, search):
            return True
    return False

def part1():
    graph = parse()
    print(graph)
    count = 0
    for outer_bag in graph.keys():
        if outer_bag is not "shiny gold" and dfs(graph, outer_bag, "shiny gold"):
            count += 1
    print(count)
        

def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

part1()
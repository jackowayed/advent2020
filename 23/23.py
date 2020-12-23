#!/usr/bin/env python3

import collections
import fileinput
import re

def rotate_to_front(l, val):
    while l[0] != val:
        l.insert(0, l.pop())

def part1():
    #input = "962713854"
    input = "389125467"
    cl = CircularList()
    for c in input:
        cl.insert_at_tail(int(c))
    cl.print_list()
    solve(cl, 100)
    cl.print_list()

def solve_p1(cups, turns):
    n_cups = len(cups)
    for turn in range(turns):
        if turn % 1000 == 0:
            print(turn)
        start = cups[0]
        pickup = cups[1:4]
        cups = cups[:1] + cups[4:]
        dest_idx = -1
        for n in range(cups[0] - 1, -1, -1):
            if n in cups:
                dest_idx = cups.index(n)
                break
        if dest_idx == -1:
            max_ = max(cups)
            dest_idx = cups.index(max_)
        old_cups = cups
        cups = cups[:dest_idx + 1] + pickup + cups[dest_idx + 1:]
        assert len(cups) == n_cups
        #    cups = old_cups[:len(cups) - n_cups] + cups
        #    print(cups)
        next_idx = (cups.index(start) + 1) % len(cups)
        rotate_to_front(cups, cups[next_idx])
    rotate_to_front(cups, 1)
    return cups


class CupNode:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class CircularList:
    def __init__(self):
        self.head = None
        self.index = dict()

    def print_list(self):
        s = str(self.head.val)
        ct = 0
        node = self.head.next
        while node.val != self.head.val:
            s += str(node.val)
            node = node.next
            ct += 1
            if ct > 20:
                break
        print(s)

    def insert_at_tail(self, val):
        if not self.head:
            self.head = CupNode(val)
            self.head.next = self.head.prev = self.head
            self.index[val] = self.head
        else:
            self.insert_after(self.head.prev, CupNode(val=val))

    def insert_after(self, node, new_node):
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        new_node.prev = node
        #if new_node.val in self.index and self.index[new_node.val] != new_node:
            #assert False, f"{new_node.val} {"
        self.index[new_node.val] = node

    def remove_after(self,node):
        rem = node.next
        node.next = rem.next
        node.next.prev = node
        return rem


N_CUPS = 1000000

def next_value(cur_val, removed_vals):
    next_val = cur_val - 1
    while next_val in removed_vals:
        next_val -= 1
    if next_val == 0:
        return N_CUPS
    else:
        return next_val

def solve(cl, turns):
    for turn in range(turns):
        removed = [cl.remove_after(cl.head) for _ in range(3)]
        removed_vals = [n.val for n in removed]
        dest_val = next_value(cl.head.val, removed_vals)
        dest_node = cl.index[dest_val]
        curr_node = dest_node
        for n in removed:
            cl.insert_after(curr_node, n)
            curr_node = n
        cl.head = cl.head.next
    cl.head = cl.index[1]


def part2():
    #input = "962713854" 
    input = "389125467"  # test
    cl = CircularList()
    for c in input:
        cl.insert_at_tail(int(c))
    for i in range(len(input), N_CUPS):
        cl.insert_at_tail(i)
    solve(cl, 10000000)
    print((cl.head.next.val, cl.head.next.next.val))
    return cl.head.next.val * cl.head.next.next.val

print(part1())
#print(part2())
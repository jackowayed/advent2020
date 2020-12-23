#!/usr/bin/env python3

import collections
import fileinput
import re

def rotate_to_front(l, val):
    while l[0] != val:
        l.insert(0, l.pop())

def part1():
    N_CUPS = 9
    input = "962713854"
    #input = "389125467"
    cl = CircularList()
    for c in input:
        cl.insert_at_tail(int(c))
    print(len(cl))
    solve(cl, 100)
    print(cl)

class CupNode:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

    def __repr__(self):
        return f"{self.val} (p {self.prev.val} n {self.next.val})"

    def __str__(self):
        return self.__repr__()


class CircularList:
    def __init__(self):
        self.head = None
        self.index = dict()

    def __repr__(self):
        s = str(self.head.val)
        ct = 0
        node = self.head.next
        while node != self.head:
            s += "," + str(node.val)
            node = node.next
            ct += 1
            if ct > 20:
                break
        return s

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        if not self.head:
            return 0
        ct = 1
        node = self.head.next
        while node != self.head:
            node = node.next
            ct += 1
        return ct


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
        assert node.next != node, node.val
        #if new_node.val in self.index and self.index[new_node.val] != new_node:
            #assert False, f"{new_node.val} {"
        self.index[new_node.val] = new_node

    def remove_after(self,node):
        rem = node.next
        node.next = rem.next
        node.next.prev = node
        return rem


N_CUPS = 1000000

def next_value(cur_val, removed_vals):
    next_val = cur_val - 1
    if next_val == 0:
        next_val = N_CUPS
    while next_val in removed_vals:
        next_val -= 1
        if next_val == 0:
            next_val = N_CUPS
    assert next_val > 0
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
    input = "962713854"
    #input = "389125467"  # test
    cl = CircularList()
    for c in input:
        cl.insert_at_tail(int(c))
    for i in range(len(input) + 1, N_CUPS + 1):
        cl.insert_at_tail(i)
    print(len(cl))
    solve(cl, 10000000)
    print(cl)
    print((cl.head.next.val, cl.head.next.next.val))
    return cl.head.next.val * cl.head.next.next.val

#print(part1())
print(part2())
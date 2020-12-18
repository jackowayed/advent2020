#!/usr/bin/env python3

import collections
import fileinput
import pdb
import re
import unittest

class Evaler:
    def __init__(self):
        self.val = None
        self.operator = None
        self.curr_token = ""
    
    def update_val(self, n):
        if not self.val:
            self.val = n
        elif self.operator == "+":
            self.val += n
        else:
            assert self.operator == "*"
            self.val *= n

    def update(self):
        if not self.curr_token:
            return
        self.update_val(int(self.curr_token))
        self.curr_token = ""



    def eval(self, it):
        #pdb.set_trace()
        for c in it:
            if c == "(":
                self.update_val(eval(it))
            elif c == ")":
                self.update()
                break
            elif c == " ":
                self.update()
            elif c == "*":
                assert next(it) == " "
                self.val *= eval(it)
            elif c == "+":
                self.operator = c
            else:
                int(c) # must be digit
                self.curr_token += c
        if self.curr_token:
            self.update()
        return self.val

def eval(s):
    return Evaler().eval(s.__iter__())


def part1():
    return sum([eval(line.strip()) for line in fileinput.input()])

def part2():
    [line.strip() for line in fileinput.input()]
    for line in fileinput.input():
        pass
    return

class Test(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(9, eval("1 + 2 * 3"))

    def test_paren(self):
        self.assertEqual(7, eval("1 + (2 * 3)"))

    def test_from_advent(self):
        self.assertEqual(eval("2 * 3 + (4 * 5)"), 46)
        self.assertEqual(eval("5 + (8 * 3 + 9 + 3 * 4 * 3)") , 1445)
        self.assertEqual(eval("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") , 669060)
        self.assertEqual(eval("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") , 23340)



unittest.main()
#print(part1())
#print(part2())
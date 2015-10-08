#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


def my_sort_v1(slist):
    was_swap = True
    while was_swap:
        was_swap = False
        for i in range(len(slist)-1):
            if slist[i] > slist[i+1]:
                slist[i], slist[i+1] = slist[i+1], slist[i]
                was_swap = True
    return slist


def my_sort_v2(slist):
    if len(slist) <= 1:
        return slist
    base_elem = slist[0]
    less_then = [elem for elem in slist if elem < base_elem]
    lerger_then = [elem for elem in slist if elem > base_elem]
    equal = [elem for elem in slist if elem == base_elem]
    return my_sort(less_then) + equal + my_sort(lerger_then)


def my_sort(slist):
    return sorted(slist)


class MySortTest(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(my_sort([4, 3, 2, 5, 5, 6, 7]), [2, 3, 4, 5, 5, 6, 7])

    def test_empty(self):
        self.assertEqual(my_sort([]), [])

    def test_single(self):
        self.assertEqual(my_sort([23]), [23])

    def test_negative(self):
        self.assertEqual(my_sort([-7, 6, -5, 4]), [-7, -5, 4, 6])

    def test_str(self):
        self.assertEqual(my_sort(['a', 'c', 'd', 'b']), ['a', 'b', 'c', 'd'])

if __name__ == '__main__':
    unittest.main()

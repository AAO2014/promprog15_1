#!/usr/bin/env python
# -*- coding: utf-8 -*-


def my_sort_v1(slist):
    was_swap = True
    while was_swap:
        was_swap = False
        for i in range(len(slist)-1):
            if slist[i] > slist[i+1]:
                slist[i],  slist[i+1] = slist[i+1],  slist[i]
                was_swap = True
    return slist


def my_sort_v2(slist):
    if len(slist) <= 1:
        return slist
    base_elem = slist[0]
    less_then = [elem for elem in slist if elem < base_elem]
    larger_then = [elem for elem in slist if elem > base_elem]
    return my_sort(less_then) + [base_elem] + my_sort(larger_then)


def my_sort(slist):
    return sorted(set(slist))




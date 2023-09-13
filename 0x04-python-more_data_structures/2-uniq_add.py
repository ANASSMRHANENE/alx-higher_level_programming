#!/usr/bin/python3
def uniq_add(my_list=[]):
    _s = set(my_list)
    sum = 0
    for n in _s:
        sum += n
    return sum

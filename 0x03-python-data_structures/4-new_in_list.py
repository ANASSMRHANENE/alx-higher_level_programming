#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    nlist = my_list.copy()
    if abs(idx) >= len(my_list):
        nlist[idx] = element
    return new_list

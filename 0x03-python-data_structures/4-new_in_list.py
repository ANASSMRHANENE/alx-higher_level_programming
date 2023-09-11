#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < -len(my_list) or idx >= len(my_list):
        return my_list.copy()
    nli = my_list[:]
    nli[idx] = element
    return nli

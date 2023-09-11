#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    def no_c(my_string):
    newstring = ""
    for c in my_string:
        if c not in "Cc":
            newstring += c
    return newstring

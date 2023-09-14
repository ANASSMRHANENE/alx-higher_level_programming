#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdic = a_dictionary.copy()
    for key, value in newdic.items():
        newdic[key] = value * 2
    return newdic

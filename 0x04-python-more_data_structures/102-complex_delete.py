#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for inndex in list(a_dictionary.keys()):
        if a_dictionary[inndex] == value:
            del a_dictionary[inndex]
    return a_dictionary

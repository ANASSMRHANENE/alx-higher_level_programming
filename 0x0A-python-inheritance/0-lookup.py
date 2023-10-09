#!/usr/bin/python3
""" 0x0A. Python """


def lookup(obj):
    """list of available attributes and methods of object

    Args:
        obj (any): object of any type

    Returns:
        list of available attributes and methods

    """
    return dir(obj)

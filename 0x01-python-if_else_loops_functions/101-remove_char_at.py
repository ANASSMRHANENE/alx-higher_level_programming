#!/usr/bin/python3
def remove_char_at(str, j):
    """Create a copy of the string without the character at position n."""
    if j < 0:
        return (str)
    return (str[:j] + str[j+1:])

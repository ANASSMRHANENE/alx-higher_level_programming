#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    j = 0
    pr = 0
    for j in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            pr += 1
        except:
            continue
    print()
    return pr

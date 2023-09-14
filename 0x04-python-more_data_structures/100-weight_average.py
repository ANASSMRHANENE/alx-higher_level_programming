#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    avrg = 0
    dv = 0
    for tup in my_list:
        avrg += tup[0] * tup[1]
        dv += tup[1]
    return float(avrg / dv)

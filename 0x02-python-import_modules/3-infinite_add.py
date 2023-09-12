#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

ar = len(sys.argv) - 1

j = 0
result = 0
for arg in sys.argv:
    if j != 0:
        r += int(arg)
    else:
        i += 1
print("{:d}".format(result))

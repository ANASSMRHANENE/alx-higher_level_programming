#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

Str = "{:d} argument"
arg = len(sys.argv) - 1
if arg == 0:
    Str += 's.'
elif arg == 1:
    Str += ':'
else:
    Str += 's:'
print(Str.format(arg))

j = 0
for arg1 in sys.argv:
    if j != 0:
        print("{:d}: {:s}".format(j, arg1))
    j += 1

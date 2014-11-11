"""
Project Euler Problem 62
========================

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
cube which has exactly three permutations of its digits which are also
cube.

Find the smallest cube for which exactly five permutations of its digits
are cube.
"""
from itertools import groupby


def main():
    cubes = (i**3 for i in xrange(8500))
    sorted_cubes = sorted(cubes, key=lambda i: sorted(str(i)))
    for k, it in groupby(sorted_cubes, key=lambda i: sorted(str(i))):
        l = list(it)
        if len(l) == 5:
            # print l
            return min(l)


if __name__ == '__main__':
    print main()

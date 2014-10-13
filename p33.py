"""
Project Euler Problem 33
========================

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""

from fractions import Fraction as F


def nontrivial(x, y):
    "Return true if input is nontrivial example"
    sx, sy = [set(divmod(i, 10)) for i in (x, y)]
    both = sx & sy
    if len(both) != 1:
        return False
    if len(sx) == len(sy) == 2 and F((sx-both).pop(), (sy-both).pop()) == F(x, y):
        return F(x, y)
    return False


def main():
    product = 1
    for x in xrange(10, 99):
        for y in xrange(x+1, 100):
            if x % 10 == 0 or y % 10 == 0:
                continue
            f = nontrivial(x, y)
            if f:
                product *= f
    return product.denominator


if __name__ == '__main__':
    print main()

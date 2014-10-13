"""
Project Euler Problem 38
========================

Take the number 192 and multiply it by each of 1, 2, and 3:

  192 * 1 = 192
  192 * 2 = 384
  192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

import itertools


def is_concatenated_product(n):
    for l in range(1, 5):
        base = int(n[:l])
        # XXX: not so restrict as for [:10]
        product = ''.join(str(base*i) for i in range(1, 10//l+1))[:10]
        if product == n:
            return True
    return False


def main():
    max_p = 0
    permutations = itertools.permutations('123456789', 9)
    for p in permutations:
        p = ''.join(p)
        if is_concatenated_product(p) and p > max_p:
            max_p = p
    print max_p


def main():
    "Faster version"
    permutations = itertools.permutations('123456789'[::-1], 9)
    for p in permutations:
        p = ''.join(p)
        if is_concatenated_product(p):
            return p


if __name__ == '__main__':
    print main()

"""
Project Euler Problem 52
========================

It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""


def has_same_digits(n):
    digits = set(str(n))
    for mul in xrange(2, 7):
        if set(str(n*mul)) != digits:
            return False
    return True


def main():
    for i in xrange(10, 10**6):
        if has_same_digits(i):
            return i
    return 'not found'

if __name__ == '__main__':
    print main()

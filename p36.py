"""
Project Euler Problem 36
========================

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""


def is_palindromic(s):
    """Return True if str `s` is palindromic."""
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i, j = i+1, j-1
    return True


def main():
    sum = 0
    for i in xrange(1, 10**6):
        di, bi = '{:d}'.format(i), '{:b}'.format(i)
        if is_palindromic(di) and is_palindromic(bi):
            sum += i
    return sum


if __name__ == '__main__':
    print main()

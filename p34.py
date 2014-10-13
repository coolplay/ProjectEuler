"""
Project Euler Problem 34
========================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial


def is_curious_number(n):
    return n == sum(factorial(int(i)) for i in str(n))


def main():
    maximum = max(n for n in range(10) if
                  factorial(9)*n > 10**(n-1))
    return sum(i for i in xrange(10, 10**(maximum-1)) if is_curious_number(i))


if __name__ == '__main__':
    print main()

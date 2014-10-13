"""
Project Euler Problem 40
========================

An irrational decimal fraction is created by concatenating the positive
integers:

                  0.123456789101112131415161718192021...
                               ^

It can be seen that the 12th digit of the fractional part is 1.

If d(n) represents the n-th digit of the fractional part, find the value
of the following expression.

    d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000)
"""

fraction = ''.join(str(i) for i in xrange(1, 500000))
assert len(fraction) >= 10**6


def d(n):
    return int(fraction[n-1])


def main():
    s = d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000)
    return s

if __name__ == '__main__':
    print main()

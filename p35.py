"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from euler import is_prime


def rotate_int(n):
    """Return a sequence of numbers by rotating integer `n` circularlly"""
    assert type(n) == int
    s = str(n)
    for i in range(len(s)):
        yield int(s[i:] + s[:i])


def main():
    count = 0
    for n in xrange(2, 1000000):
        for each in rotate_int(n):
            if not is_prime(each):
                break
        else:
            count += 1
            # print n
    print count

if __name__ == '__main__':
    main()

"""
Project Euler Problem 47
========================

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors
are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""

from euler import is_prime, prime
maximum = 10**6
# much quicker to store a list than calculate for each n
primes = list(prime(10**4))


def has_prime_factor(n, np=2, nc=2):
    """Return True if `nc` ints beginning with `n` has `np` prime factors.
    """
    if nc == 0:
        return True
    t = n
    pd = set()
    if is_prime(t):
        return False
    for d in primes:
        while t % d == 0:
            t = t // d
            pd.add(d)
        if t < d:
            break
    if len(pd) == np:
        return has_prime_factor(n+1, np, nc-1)
    return False


def main():
    for i in xrange(1, maximum):
        if has_prime_factor(i, 4, 4):
            return i


if __name__ == '__main__':
    print main()

"""Quadratic primes"""
import functools
import operator
from euler import is_prime

def consecutive_primes(a, b):
    """Return consecutive number of primes for formula determined by `a` and
    `b`"""
    f = lambda n: n**2 + a*n + b
    n = 0
    while True:
        if is_prime(f(n)):
            n += 1
        else:
            break
    return n + 1, a, b


N = 1000
mitem = max(consecutive_primes(a, b) for a in xrange(-N+1, N)
                                     for b in xrange(-N+1, N))
print(functools.reduce(operator.mul, mitem[1:]))


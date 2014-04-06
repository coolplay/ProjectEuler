"""Smallest multiple"""
from p3 import prime

N = 20
primes = list(prime(N+1))
for i in range(2, N+1):
    prime_factor = []
    for p in primes:
        while i % p == 0:
            prime_factor.append(p)
            if i == p:
                break
            i = i / p
        if i == p: break
    for each in set(prime_factor):
        if prime_factor.count(each) > primes.count(each):
            primes.extend([each]*(prime_factor.count(each) - primes.count(each)))

import operator
import functools
print(functools.reduce(operator.mul, primes))

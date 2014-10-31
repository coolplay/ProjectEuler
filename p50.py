"""
Project Euler Problem 50
========================

The prime 41, can be written as the sum of six consecutive primes:

                       41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""
#XXX: time too long
from euler import prime, is_prime
from bisect import bisect_left


def main(N):
    primes = list(prime(N))
    sums = [sum(primes[:i]) for i in xrange(len(primes)+1)]

    longest, indices = 0, (0, 0)
    for i, si in enumerate(sums):
        j = bisect_left(sums, si+N) - 1
        for j in xrange(j, i+longest, -1):
            sj = sums[j]
            if is_prime(sj - si):
                if j - i > longest:
                    longest = j - i
                    indices = i, j
                    break
    return sums[indices[1]]-sums[indices[0]]


if __name__ == '__main__':
    print main(10**6)

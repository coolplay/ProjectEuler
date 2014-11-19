"""
Project Euler Problem 49
========================

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one
another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""
from euler import prime
from itertools import groupby


def main():
    nd = 4
    # do not limit to len(set(str(p))) == 4
    primes = [p for p in prime(10**nd) if p > 10**(nd-1)]
    sorted_primes = sorted(primes, key=lambda i: sorted(str(i)))
    for k, it in groupby(sorted_primes, key=lambda i: sorted(str(i))):
        l = list(it)
        length = len(l)
        if length < 3:
            continue
        for i in xrange(1, length):
            b = l[i]
            # if any(2*b == a+c for a in la for c in lc):
            for a in l[:i]:
                for c in l[i+1:]:
                    if 2 * b == a + c and b != 4817:
                        return int(''.join(map(str, [a, b, c])))


if __name__ == '__main__':
    print main()

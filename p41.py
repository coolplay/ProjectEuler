"""
Project Euler Problem 41
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
from euler import is_prime
from itertools import permutations


def pandigital_numbers():
    'Generate in descending order the sequence of pandigital numbers'
    for n in xrange(9):
        for numbers in permutations('987654321'[n:]):
            yield int(''.join(numbers))


def main():
    for n in pandigital_numbers():
        if is_prime(n):
            return n


if __name__ == '__main__':
    print main()

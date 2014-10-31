"""
Project Euler Problem 46
========================

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""
from euler import is_prime


def odd_composite():
    i = 9
    while True:
        if not is_prime(i):
            yield i
        i += 2


def main():
    for i in odd_composite():
        j = 1
        while True:
            remain = i - 2*j**2
            if remain <= 1:
                return i
            if is_prime(remain):
                break
            j += 1


def main2():
    for i in odd_composite():
        if any(is_prime(i - 2*j**2) for j in xrange(i) if i - 2*j**2 > 1):
            continue
        return i

if __name__ == '__main__':
    print main()

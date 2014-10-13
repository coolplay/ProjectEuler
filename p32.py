"""
Project Euler Problem 32
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""


def is_pandigital(s):
    "Return True if str `s` is pandigital."""
    return set(s) == set('123456789')


def main():
    products = set()
    for i in xrange(2, 100):
        for j in xrange(i+1, 5000):
            product = i * j
            digits = ''.join(str(n) for n in [i, j, product])
            if len(digits) != 9:
                continue
            if is_pandigital(digits):
                products.add(product)
    return sum(products)


if __name__ == '__main__':
    print main()

"""
Project Euler Problem 57
========================

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

            2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in
the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a
numerator with more digits than denominator?
"""
from fractions import Fraction


class memoize:
    'You will be eaten up without this'
    # http://avinashv.net/2008/04/python-decorators-syntactic-sugar/
    def __init__(self, function):
        self.function = function
        self.memoized = {}

    def __call__(self, *args):
        try:
            return self.memoized[args]
        except KeyError:
            self.memoized[args] = self.function(*args)
            return self.memoized[args]


@memoize
def f(n):
    "Return nth expansion of sqrt(2)"
    if n == 1:
        return Fraction(3, 2)
    return (f(n-1)+2) / (f(n-1)+1)


def main():
    return sum(len(str(f(n).numerator)) > len(str(f(n).denominator))
               for n in xrange(1, 1000))

if __name__ == '__main__':
    print main()

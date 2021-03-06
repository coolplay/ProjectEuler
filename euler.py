"""Helper functions for Project Euler"""
import math
import operator
import itertools
import bisect

def fibonacci(maximum):
    """Generate sequece of Fibonacci numbers no larger than `maximum`"""
    i, j = 1, 2
    if maximum <= 1:
        return
    else:
        yield i
    while j < maximum:
        yield j
        i, j = j, i+j


def prime(maximum):
    """Generate sequence of prime numbers up to `maximum`"""
    if maximum < 2: return
    for i in xrange(2, maximum):
        # if i <= 3:
            # yield i
            # continue
        # elif i == 4:
            # continue
        for j in xrange(2, int(i**0.5)+1):
            if i % j == 0: break
        else:
            # That's a prime!
            yield i

def is_prime(number):
    """Return True if `number` is prime"""
    i = number
    if i <= 1 or not isinstance(i, (int, long)):
        return False
    for j in xrange(2, int(i**0.5)+1):
        if i % j == 0:
            return False
    return True

def nchoosek(n, k):
    """Returns the binomial coefficient"""
    fact = math.factorial
    return fact(n)//fact(k)//fact(n-k)

    # if n < 0 or k < 0:
        # raise Exception('Non negative number required!')
    # if n < k:
        # return 0
    # return (reduce(operator.mul, (i for i in xrange(n, n-k, -1))) /
        # reduce(operator.mul, (i for i in xrange(1, k+1))))

def sumofdigits(integer):
    """Return sum of digits in integer"""
    assert integer > 0
    s = str(integer)
    return sum(int(i) for i in list(s))

def divisor(integer, self=True):
    """Generate divisor sequence of positive int `integer` increasingly"""
    assert integer > 0
    for i in range(1, integer+self):
        if integer % i == 0:
            yield i


def get_digits(i):
    """Generate a sequence of digits from integer `i` in reversed order

    """
    assert i >= 0 and isinstance(i, (int, long))
    digits = []
    while i >= 10:
        i, r = divmod(i, 10)
        digits.append(r)
    digits.append(i)
    return reversed(digits)


def str_digits(i):
    """Return str type of integer `i`"""
    return str(i)
    # Same as get_digits
    # return map(int, list(str(i)))


def is_palindromic(s):
    """Return True if str `s` is palindromic."""
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i, j = i+1, j-1
    return True


# Modified from Python docs for bisect
def binsearch(a, x):
    'Locate the leftmost value exactly equal to x in sorted sequence `a`'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1


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


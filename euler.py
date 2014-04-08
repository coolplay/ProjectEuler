"""Helper functions for Project Euler"""
import math
import operator
import itertools

def prime(maximum):
    """Generate sequence of prime numbers up to `maximum`"""
    if maximum < 2: return
    for i in xrange(2, maximum):
#       if i <= 3:
#           yield i
#           continue
#       elif i == 4:
#           continue
        for j in xrange(2, int(i**0.5)+1):
            if i % j == 0: break
        else:
            # That's a prime!
            yield i

def nchoosek(n, k):
    """Returns the binomial coefficient"""
    fact = math.factorial
    return fact(n)//fact(k)//fact(n-k)

#   if n < 0 or k < 0:
#       raise Exception('Non negative number required!')
#   if n < k:
#       return 0
#   return (reduce(operator.mul, (i for i in xrange(n, n-k, -1))) /
#       reduce(operator.mul, (i for i in xrange(1, k+1))))

def sumofdigits(integer):
    """Return sum of digits in integer"""
    assert integer > 0
    s = str(integer)
    return sum(int(i) for i in list(s))

def divisor(integer):
    """Generate divisor sequence of positive int `integer` increasingly"""
    assert integer > 0
    for i in range(1, integer+1):
        if integer % i == 0:
            yield i


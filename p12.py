"""Highly divisible triangular number"""

def triangle_number(n=20000):
    """Generate first `n` triangle number"""
    for i in xrange(1, n):
        yield (i+1)*i/2


for n in triangle_number():
    count = 0
    for i in xrange(1, n+1):
        if n % i == 0:
            j = n / i
            count += 1
            if j < i:
                count = 2 * (count - 1)
                break
            elif j == i:
                count = 2 * count - 1
                break
    if count > 500:
        print """The first triangle number to have over five hundred divisors ({}) is: {}""".format(count, n)
        break





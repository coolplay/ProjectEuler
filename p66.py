"""
Project Euler Problem 66
========================

Consider quadratic Diophantine equations of the form:

                              x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13 * 180^2 =
1.

It can be assumed that there are no solutions in positive integers when D
is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

3^2 - 2 * 2^2 = 1
2^2 - 3 * 1^2 = 1
9^2 - 5 * 4^2 = 1
5^2 - 6 * 2^2 = 1
8^2 - 7 * 3^2 = 1

Hence, by considering minimal solutions in x for D 7, the largest x is
obtained when D=5.

Find the value of D 1000 in minimal solutions of x for which the largest
value of x is obtained.
"""
# http://en.wikipedia.org/wiki/Chakravala_method#The_method
from math import sqrt


def init(d):
    "Return init int parameters for x^2 + dy^2 = k, with min(abs(k)) required"
    b = 1
    a = int(sqrt(d))
    k1, k2 = a**2 - d, (a+1)**2 - d
    if abs(k1) < abs(k2):
        k = k1
    else:
        k = k2
        a += 1
    # print a, b, k
    return a, b, k


def new(a, b, k, d):
    "Generate parameters in next step"
    absk = abs(k)
    # get r
    r = 0
    while (b*r + a % absk) % absk != 0:
        r += 1
    # get m
    m = int(sqrt(d))
    t = (m-r) // absk
    m1, m2 = absk * t + r, absk * (t+1) + r
    if abs(m1**2 - d) < abs(m2**2 - d):
        m = m1
    else:
        m = m2
    # get triple
    a, b, k = (a*m + d*b)/absk, (a + b*m)/absk, (m**2 - d)/k
    return a, b, k


def main():
    maxa = 0
    for d in xrange(2, 1001):
        if sqrt(d) == int(sqrt(d)):
            continue
        a, b, k = init(d)
        while k != 1:
            a, b, k = new(a, b, k, d)
        if a > maxa:
            maxa = a
            maxd = d
    return maxd


if __name__ == '__main__':
    print main()

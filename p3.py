"""Largest prime factor"""
from euler import prime

#M = int(raw_input('Input the integer: '))
#if M < 2: print 'Invalid integer'
M = 600851475143
N = M
# p: prime number no bigger than N
for p in prime(N+1):
    while N % p == 0:
        if N == p:
            print 'Largest prime factor of number {} is: {}'.format(M, p)
            raise SystemExit
        N = N / p




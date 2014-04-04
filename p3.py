"""Largest prime factor"""
def prime(maximum):
    """Generate sequence of prime numbers less than `maximum`"""
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

M = int(raw_input('Input the integer: '))
if M < 2: print 'Invalid integer'
N = M
# p: prime number no bigger than N
for p in prime(N+1):
    while N % p == 0:
        if N == p:
            print 'Largest prime factor of number {} is: {}'.format(M, p)
            raise SystemExit
        N = N / p




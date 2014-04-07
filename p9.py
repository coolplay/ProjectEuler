"""Special Pythagorean triplet"""
N = 1000
#for a in xrange(N//3):
#    for b in xrange(a+1, N//2):
#        if 10**6 + 2*a*b == 2000*(a + b):
for a in xrange(1, N):
    for b in xrange(a+1, N):
        c = N - (a + b)
        if a**2 + b**2 == c**2:
            print '{}*{}*{} = {}'.format(a, b, c, a*b*c)

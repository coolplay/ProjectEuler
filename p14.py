"""Longest Collatz sequence"""

def collatz(n):
    """Generate collatz sequence starting from `n`, which always ends with 1"""
    assert isinstance(n, (int, long)) and n > 1
    while n != 1:
        yield n
        n = n//2 if n % 2 == 0 else 3*n+1
    yield n

N = 10**6
maximum = 0
for i in xrange(2, N):
    length = len(list(collatz(i)))
    if length > maximum:
        maximum = length
        starting = i
print "Starting number {} has longest collatz sequence: {}".format(starting,
        maximum)


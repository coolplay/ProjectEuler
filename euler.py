"""Helper functions for Project Euler"""

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


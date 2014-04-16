"""Reciprocal cycles"""
def cycle_length(n):
    """Return length of recurring cycle of fraction 1/n"""
    i = 1
    remainder = {i}
    i = 10 * i % n
    while i not in remainder:
        remainder.add(i)
        i = 10 * i % n
    return len(remainder)

N = 20000
maximum = 0
# 1.
#for denominator in range(2, N):
#    recurring_length = cycle_length(denominator)
#    if recurring_length > maximum:
#        maximum = recurring_length
#        d = denominator
# 2.
#maximum, d = max((cycle_length(i), i) for i in xrange(2, N))

print('Largest denominator in range({}) is: {}'.format(N, d))


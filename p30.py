"""Digit fifth powers"""
from euler import get_digits

def is_npower_number(i, n=4):
    """Return True if sum of `n`th power of digits in `i` equates `i`"""
    assert i > 1
    return i == sum(a**n for a in get_digits(i))

# Actually the upper bound N of n power number can be roughly determined.
def upper_bound(n=5):
    """Determine upper bound of the `n` power number"""
    x = 0
    while (x+1) * 9**5 >= 10**x:
        x += 1
    return 10**x

N = 1000000
print(sum(i for i in xrange(2, N) if is_npower_number(i, n=5)))



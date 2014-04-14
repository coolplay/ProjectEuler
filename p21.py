"""Amicable numbers"""
from euler import divisor

def d(n):
    """Sum of proper divisor of `n`"""
    return sum(divisor(n)) - n

N = 10000
amicable = set()
for a in range(3, N):
    if a in amicable:
        continue
    b = d(a)
    if a != b and d(b) == a:
        amicable.update({a, b})
print sum(amicable)

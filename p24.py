"""Lexicographic permutations"""
import math

def nth_permutation(index, digits=10):
    """Find `index`th lexicographic permutation with `digits` digit"""
    index -= 1
    a = range(digits)
    res = []
    # Relation between index and item
    for n in range(digits-1, 0, -1):
        # idx is index of list `a`
        idx, index = divmod(index, math.factorial(n))
        res.append(a.pop(idx))
    res.append(a.pop())
    return (''.join(str(i) for i in res))
    #return int(''.join(str(i) for i in res))

print nth_permutation(10**6)

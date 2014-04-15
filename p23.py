"""Non-abundant sums"""
import itertools

def abundant_number(maximum):
    """Generate sequence of abundant numbers up to `maximum`"""
    for i in xrange(2, maximum, 1):
        divisor = {1}
        for j in xrange(2, int(i**0.5)+1):
            if i % j == 0:
                r = i // j
                divisor.update({j, r})
        # abundant
        if i < sum(divisor):
            yield i

def sum2item(sequence):
    """Return set of 2-item sums in `sequence`"""
    comb = itertools.combinations
    sequence = set(sequence)
    # combination from 2 different items
    res = {sum(i) for i in comb(sequence, 2)}
    # combination from 2 same items
    res.update({2*i for i in sequence})
    return res

if __name__ == '__main__':
    N = 28123
    n = sum2item(abundant_number(N))
    res = set(range(N+1)) - n
    print(sum(res))


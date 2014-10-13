"""
Project Euler Problem 37
========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from euler import is_prime


def remove_digits(i):
    """Generate sequence of ints(>0) by removing digits of i from both side"""
    digits = set()
    j, e = i, 1
    j, r = divmod(i, 10**e)
    while j > 0:
        digits.update((j, r))
        e += 1
        j, r = divmod(i, 10**e)
    return digits - {0}


def main():
    targets = []
    i = 10
    while len(targets) != 11:
        if is_prime(i):
            for j in remove_digits(i):
                if not is_prime(j):
                    break
            else:
                targets.append(i)
        i += 1
    # show results
    print sum(targets)
    # print '{} truncatable primes: {}'.format(len(targets), targets)


if __name__ == '__main__':
    main()

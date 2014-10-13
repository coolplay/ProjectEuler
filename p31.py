"""
Project Euler Problem 31
========================

In England the currency is made up of pound, -L-, and pence, p, and there
are eight coins in general circulation:

  1p, 2p, 5p, 10p, 20p, 50p, -L-1 (100p) and -L-2 (200p).

It is possible to make -L-2 in the following way:

  1 * -L-1 + 1 * 50p + 2 * 20p + 1 * 5p + 1 * 2p + 3 * 1p

How many different ways can -L-2 be made using any number of coins?
"""

coins = [200, 100, 50, 20, 10, 5, 2, 1]


def p(target=200, level=0):
    "Recursion"
    coin = coins[level]
    if coin == 1:
        return 1
    count = 0
    for current in range(0, target+1, coin):
        count += p(target-current, level+1)
    return count


if __name__ == '__main__':
    print p()

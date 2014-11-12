"""
Project Euler Problem 63
========================

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the
9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""


def main():
    # 10^(n-1/n), 10^(n/n)
    min, max = 0, 10
    number = 0
    nth = 1
    while True:
        if max == min:
            return number
        min = 10 ** (float(nth-1)/nth)
        min = int(min) + (int(min) != min)
        number += max - min
        nth += 1


if __name__ == '__main__':
    print main()

"""10001st prime"""
from euler import prime

N = 10001
M = 10**6
for index, number in enumerate(prime(M), start=1):
    if index  == N:
        print number
        break


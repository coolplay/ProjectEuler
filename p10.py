"""Summation of primes"""
import euler

N = 2*10**6
print sum(i for i in euler.prime(N))

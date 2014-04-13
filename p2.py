"""Even Fibonacci numbers"""
from euler import fibonacci

#1. direct way
print(sum(i for i in fibonacci(4000000) if i % 2 == 0))

#2. every third number is even

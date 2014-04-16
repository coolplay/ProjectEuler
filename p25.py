"""1000-digit Fibonacci number"""
from euler import fibonacci

N = 1000
maximum = 10**1001
for idx, i in enumerate(fibonacci(maximum), start=2):
    if len(str(i)) == N:
        print '{}th term contains 1000 digits: \n{}'.format(idx, i)
        break

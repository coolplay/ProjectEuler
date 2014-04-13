"""Multiples of 3 and 5"""
# 1.
N = 1000
print(sum(i for i in range(N) if i%3 == 0 or i%5 == 0))

# 2. sum(set3 | set5)
def setn(n, N):
    """Return set with positive members evenly divisible by `n` up to `N`"""
    return {i*n for i in range(1, (N-1)//n+1)}

print sum(setn(3, N) | setn(5, N))

# 3. We could also solve it analytically.

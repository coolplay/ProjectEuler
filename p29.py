"""Distinct powers"""

N = 100
print(len({a**b for a in range(2, N+1) for b in range(2, N+1)}))

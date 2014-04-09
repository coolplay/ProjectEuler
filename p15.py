"""Lattice paths

Count ways of combining 20 `right` and 20 `down`
"""
from euler import nchoosek

N = 40
print(nchoosek(N, N/2))

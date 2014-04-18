"""Number spiral diagonals"""

def sum_spiral_diagonal(N):
    """Return sum of `N`*`N` spiral diagonals.

    sum of outmost elements in diagonals of N*N spiral:
        2*(2*N**2 - 3*N +3)
    """
    assert N % 2 != 0
    return sum(2*(2*i**2-3*i+3) for i in xrange(3, N+1, 2)) + 1

N = 1001
print(sum_spiral_diagonal(N))




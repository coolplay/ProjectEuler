"""Sum square difference"""
def sum_of_square(n):
    """\sum_{i=1,n} i^2 = n(n+1)(2*n+1)/6"""
    if isinstance(n, int) and n > 0:
        return n*(n+1)*(2*n+1)/6

def square_of_sum(n):
    """(\sum_{i=1,n} i)^2 = ((1+n)*n/2)**2"""
    if isinstance(n, int) and n > 0:
        return ((1+n)*n/2)**2

N = 100
print(square_of_sum(N) - sum_of_square(N))


"""
Project Euler Problem 67
========================

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                    3
                                   7 4
                                  2 4 6
                                 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not
possible to try every route to solve this problem, as there are 2^99
altogether! If you could check one trillion (10^12) routes every second it
would take over twenty billion years to check them all. There is an
efficient algorithm to solve it. ;o)
"""
from euler import memoize

tri = [[int(n) for n in line.split()] for line in open('triangle.txt')]


# XXX other methods besides recursive
# max total below a node is node + maxroute under the node
@memoize
def maxroute(i, j):
    'Return max total of routes below node[i, j]'
    if i == 99:
        return 0
    return max(tri[i+1][j+0] + maxroute(i+1, j+0),
               tri[i+1][j+1] + maxroute(i+1, j+1))


def main():
    return tri[0][0] + maxroute(0, 0)

if __name__ == '__main__':
    print main()

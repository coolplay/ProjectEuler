"""
Project Euler Problem 39
========================

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
"""


def solutions(p):
    "Return sequence of sides of right angle triangle, with a<b<c"
    solution = []
    for a in xrange(1, p//2+1):
        b = int(0.5*p*(p-2*a)/(p-a))
        if a > b:
            continue
        c = p - a - b
        if a**2 + b**2 == c**2:
            solution.append((a, b, c))
    return solution


def main():
    max_solutions = 0
    for p in xrange(4, 1000):
        s = len(solutions(p))
        if s > max_solutions:
            max_solutions = s
            max_p = p
    print max_p
#   print solutions(max_p)

if __name__ == '__main__':
    main()

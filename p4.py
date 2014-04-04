"""Largest palindrome product"""
def is_palindrome(number):
    l = str(number)
    for i in range(len(l)//2):
        # string is also iterable
        if l[i] != l[-1-i]: return False
    return True

#for i in range(999, 100, -1):
#    for j in range(i, 99, -1):
#995*583=580085 isn't the answer. Dont't be silly!
maximum = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        res = i * j
        if is_palindrome(res) and res > maximum:
            maximum = res
            mi, mj = i, j
print 'Largest palindrome product is: {}*{}={}'.format(mi, mj, maximum)

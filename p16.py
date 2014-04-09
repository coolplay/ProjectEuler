"""Power digit sum"""
N = 2**1000
print sum(int(i) for i in str(N))

# or in full functional way:
print(sum(map(int, str(pow(2, 1000)))))

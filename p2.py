"""Even Fibonacci numbers"""

def fibonacci(maximum):
    """Generate sequece of Fibonacci numbers no larger than `maximum`"""
    i, j = 1, 2
    if maximum <= 1:
        return
    else:
        yield i
    while j < maximum:
        yield j
        i, j = j, i+j

print(sum(i for i in fibonacci(4000000) if i % 2 == 0))

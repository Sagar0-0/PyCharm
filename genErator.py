def factorial(n):
    sum = 1
    for i in range(n, 0, -1):
        sum = sum * i
    yield sum


def fibonacci(nterms):
    n1, n2 = 0, 1
    for i in range(nterms):
        yield n1
        nth = n1 + n2
        n1 = n2
        n2 = nth


g = fibonacci(80)
for i in g:
    print(i)

def factorial (n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

print(factorial(3))

def factorial_loop(n):
    a = 1
    for i in range(2, n + 1):
        a = a * i
    return a

print(factorial_loop(5)) 
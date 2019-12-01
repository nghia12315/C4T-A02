def fibonacci(n):
    if n < 2:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return c

print(fibonacci(4))

def fibonacci_recursion(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci_recursion(6))  

    
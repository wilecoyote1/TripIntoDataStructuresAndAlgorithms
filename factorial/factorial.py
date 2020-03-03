def factorial(n):
    sum = 1
    for i in range(2,n+1):
        sum *= i
    return sum

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
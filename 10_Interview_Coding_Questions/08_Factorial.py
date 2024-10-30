def factorial(n):
    res = 1
    for i in range(n, 0, -1):
        res *= i
    return res


print(factorial(3))  # returns 6
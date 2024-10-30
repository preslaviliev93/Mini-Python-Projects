"""
Print Fibonacci sequence
"""


def fibonacci(n):
    result = []
    first, second = 0, 1
    for i in range(n):
        result.append(first)
        first, second = second, first + second
    return f"{', '.join(map(str, result))}"


print(fibonacci(15))

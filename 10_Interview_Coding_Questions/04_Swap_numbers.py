"""
Swap two numbers without using third variable.
"""


def swap(num1, num2):
    num1, num2 = num2, num1
    return num1, num2


print(swap(1, 2))
print(swap(4, 6))
print(swap(2, 8))

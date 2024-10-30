"""
Write a function that takes an integer as an argument and returns the reversed integer.
"""


# Method 1

def reverse(x):
    reversed_num = 0
    while x != 0:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    return reversed_num


# Method 2
def reverse_num(x):
    num = str(x)
    reversed_num = int(num[::-1])
    return reversed_num


print(reverse(10))
print(reverse(103))
print(reverse_num(10))
print(reverse_num(103))

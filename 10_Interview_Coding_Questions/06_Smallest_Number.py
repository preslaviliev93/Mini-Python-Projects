"""
Write a program which finds the smallest number.
The program should take unlimited number of parameters.
"""


def find_smallest(*args):
    all_nums = list(args)
    return f"Smallest number: {min(all_nums)}"


print(find_smallest(10, -45, 19))

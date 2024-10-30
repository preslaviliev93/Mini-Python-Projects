"""
Find the second largest element in a list
"""
from random import randint


def get_second_largest(in_lst):
    in_lst.remove(max(in_lst))
    return max(in_lst)


test_lst = [randint(1, 100) for n in range(10)]
print(f'Test list: {test_lst}')
print(f"Second largest element: {get_second_largest(test_lst)}")

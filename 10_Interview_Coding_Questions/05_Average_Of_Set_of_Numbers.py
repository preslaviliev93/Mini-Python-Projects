"""
Find the average of all numbers in a set.
"""

set_of_numbers = set([100, 10000, 42045, 45679, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9])


def get_avg(set_of_numbers):
    return f"{sum(set_of_numbers) / len(set_of_numbers)}"


def get_avg_pretty(set_of_numbers):
    total_avg = sum(set_of_numbers) / len(set_of_numbers)
    return f"{total_avg:.2f}"

print(get_avg(set_of_numbers))

print(get_avg_pretty(set_of_numbers))
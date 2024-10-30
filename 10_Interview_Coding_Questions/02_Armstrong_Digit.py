"""
It is a number which is equal to the sum of cube of its digits.
"""

def is_armstrong_number(number):
    digits_sum = 0
    digits = list(map(int, str(number)))
    for num in digits:
        digits_sum += num**3
    return f"Number {number} is Armstrong?:  {digits_sum == number}"




 ### Tests ###

print(is_armstrong_number(10))
print(is_armstrong_number(153))
print(is_armstrong_number(370))
print(is_armstrong_number(355))


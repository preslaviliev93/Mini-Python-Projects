from math import sqrt


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for index in range(3, int(sqrt(n)) + 1, 2):
        if n % index == 0:
            return False

    return True


print(is_prime(11))

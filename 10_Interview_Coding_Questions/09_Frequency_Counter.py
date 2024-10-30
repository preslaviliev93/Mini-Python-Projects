"""
Count the frequency of each element in a list
"""
def frequency(lst):
    res = {}
    for item in lst:
        if item not in res:
            res[item] = 0
        res[item] += 1
    return res



# Tests
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
print("".join(f"{k} -> {v} times\n" for k, v in frequency(nums).items()))
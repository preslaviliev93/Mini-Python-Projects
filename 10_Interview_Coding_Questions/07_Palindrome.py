"""
Write a program which checks if a given string is palindrome or not.
"""


def is_palindrome(string):
    return string == string[::-1]



# Test Function
test_case = ['test', 'madam', 'not a palindrome', 'wow']
for word in test_case:
    print(f"Is \"{word}\" palindrome: {is_palindrome(word)}")
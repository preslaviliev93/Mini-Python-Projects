"""
You will be provided a lower case letter.
The program must print the position of the letter in the alphabet.
"""


# 97 -> a

def find_position(letter):
    return ord(letter) - 96


print(find_position('b'))

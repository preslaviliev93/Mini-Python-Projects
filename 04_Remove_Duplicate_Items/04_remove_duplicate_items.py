# The test string will contain Duplicate words
# test_string = ("milk, eggs, bread, butter, cheese, apples, oranges, bananas, chicken, beef, pork, rice,"
#                " pasta, tomatoes, onions, garlic, potatoes, carrots, cucumbers, lettuce, spinach, mushrooms,"
#                " milk, eggs, cheese, yogurt, fish, shrimp, olive oil, salt, pepper, sugar, flour, baking powder, soda,"
#                " chips, crackers, cereal, juice, coffee, tea, honey, jam, peanut butter, oats, bananas, oranges,"
#                " chicken, beef, pasta, cheese, yogurt, milk, eggs, bread, sugar, rice, potatoes, tomatoes, onions,"
#                " garlic, spinach, butter, apples, fish, shrimp, cucumbers, lettuce, olive oil, chips,"
#                " crackers, cereal, juice")


def remove_duplicate_items(in_string, split_delimiter):
    removed_duplicates = in_string.split(split_delimiter)
    return set(removed_duplicates)


test_str = input("Enter a string with duplicate words: ")
delimiter = input("Enter delimiter: ")
result = remove_duplicate_items(test_str, delimiter)
print("\n".join(result))

"""
This script will count the:
    1. Number of words
    2. Number of characters
    3. Number of lines
"""


class Counter:
    def __init__(self, file_location):
        self.file_location = file_location

    def read_file(self):
        try:
            with open(self.file_location, 'r') as f:
                contents = f.read()
            return contents
        except FileNotFoundError:
            return f'File {self.file_location} not found'

    def count_words(self):
        return len(self.read_file().split())

    # This method WILL NOT count white spaces ( ), lines (\n) and tabs (\t)
    def count_characters(self):
        char_counter = 0
        for char in self.read_file():
            if char not in [' ', '\n', '\t']:
                char_counter += 1
        return char_counter

    def count_lines(self):
        return len(self.read_file().split('\n'))

    def main(self):
        content = self.read_file()
        print(f'There are {self.count_words()} words in the file.')
        print(f'There are {self.count_characters()} characters in the file.')
        print(f'There are {self.count_lines()} lines in the file.')


if __name__ == "__main__":
    file = input()
    counter = Counter(file)
    counter.main()

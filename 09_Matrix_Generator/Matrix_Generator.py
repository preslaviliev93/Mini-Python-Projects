import random
"""
    This class returns a matrix with random int numbers.
    The size of the matrix is taken based on the users' specifications
"""

class MatrixGenerator:
    def __init__(self, matrix_cols, matrix_rows, start_number, end_number):
        self.matrix_cols = matrix_cols
        self.matrix_rows = matrix_rows
        self.start_number = start_number
        self.end_number = end_number


    def generate(self):
        matrix = [[random.randint(self.start_number, self.end_number) for _ in range(self.matrix_cols)] for _ in
                  range(self.matrix_rows)]

        return matrix

    def pretty_print(self):
        pretty = ''
        matrix = self.generate()
        for row in matrix:
            pretty += f" ".join(f"{num}" for num in row) + "\n"

        pretty += f"\nList View:\n{matrix}"

        return pretty


matrix_generator = MatrixGenerator(3, 2, 10, 50)
# print("\nPRETTY RANDOM MATRIX GENERATOR")
# matrix_generator.pretty_print()
print("\nMatrix Generator")
print(matrix_generator.pretty_print())


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
        # Generate and pretty print the matrix
        matrix = self.generate()
        for row in matrix:
            print(" ".join(f"{num}" for num in row))


matrix_generator = MatrixGenerator(6, 6, 10, 50)
print(matrix_generator.generate())
print("\nPRETTY")
matrix_generator.pretty_print()


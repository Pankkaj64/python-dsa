from typing import List


def generate(num_rows: int) -> List[List[int]]:
    """
    Generate the first num_rows of Pascal's Triangle.
    """

    triangle = []

    for row in range(num_rows):
        current_row = [1] * (row + 1)

        for j in range(1, row):
            current_row[j] = (
                triangle[row - 1][j - 1]
                + triangle[row - 1][j]
            )

        triangle.append(current_row)

    return triangle
import unittest

from main import generate


class TestPascalTriangle(unittest.TestCase):

    def test_one_row(self):
        self.assertEqual(
            generate(1),
            [[1]]
        )

    def test_five_rows(self):
        self.assertEqual(
            generate(5),
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1]
            ]
        )

    def test_zero_rows(self):
        self.assertEqual(
            generate(0),
            []
        )

    def test_two_rows(self):
        self.assertEqual(
            generate(2),
            [
                [1],
                [1, 1]
            ]
        )

    def test_ten_rows(self):
        result = generate(10)

        self.assertEqual(len(result), 10)
        self.assertEqual(
            result[9],
            [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
        )


if __name__ == "__main__":
    unittest.main()
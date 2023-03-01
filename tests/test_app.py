import unittest

from app import get_solution

class TestApp(unittest.TestCase):

    def test_image_to_solution(self):
        expected = [
            [8, 2, 1, 5, 6, 7, 9, 3, 4],
            [3, 9, 7, 4, 2, 1, 8, 5, 6],
            [6, 4, 5, 9, 3, 8, 7, 1, 2],
            [5, 7, 4, 8, 1, 6, 3, 2, 9],
            [2, 1, 8, 3, 9, 4, 6, 7, 5],
            [9, 3, 6, 7, 5, 2, 4, 8, 1],
            [1, 8, 2, 6, 7, 9, 5, 4, 3],
            [7, 6, 3, 1, 4, 5, 2, 9, 8],
            [4, 5, 9, 2, 8, 3, 1, 6, 7]
        ]
        path = 'images/s1.PNG'
        solution = get_solution(path)
        self.assertEqual(solution, expected)

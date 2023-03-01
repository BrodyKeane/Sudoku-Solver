import unittest

from solver import Solver
from sudoku import Sudoku


class TestSudokuSolver(unittest.TestCase):
    def test_basic_row_solve(self):
        tiles = [
            [0, 3, 4, 6, 7, 8, 9, 1, 2],
            [0, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        sudoku = Sudoku(tiles)
        solver = Solver(sudoku)
        solver.solve()
        self.assertTrue(sudoku.is_solved())


    def test_multiple_basic_row_solve(self):
        tiles = [
            [0, 3, 4, 6, 7, 8, 9, 1, 2],
            [0, 7, 2, 1, 9, 5, 3, 4, 8],
            [0, 9, 8, 3, 4, 2, 5, 6, 7],
            [0, 5, 9, 7, 6, 1, 4, 2, 3],
            [0, 2, 6, 8, 5, 3, 7, 9, 1],
            [0, 1, 3, 9, 2, 4, 8, 5, 6],
            [0, 6, 1, 5, 3, 7, 2, 8, 4],
            [0, 8, 7, 4, 1, 9, 6, 3, 5],
            [0, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        sudoku = Sudoku(tiles)
        solver = Solver(sudoku)
        solver.solve()
        self.assertTrue(sudoku.is_solved())



    def test_basic_column_solve(self):
        tiles = [
            [0, 0, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        sudoku = Sudoku(tiles)
        solver = Solver(sudoku)
        solver.solve()
        self.assertTrue(sudoku.is_solved())

    def test_multiple_basic_column_solve(self):
        tiles = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        sudoku = Sudoku(tiles)
        solver = Solver(sudoku)
        solver.solve()
        self.assertTrue(sudoku.is_solved()) 

    def test_basic_subgrid_solve(self):
        tiles = [
            [0, 3, 4, 0, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [0, 5, 9, 0, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        sudoku = Sudoku(tiles)
        solver = Solver(sudoku)
        solver.solve()
        self.assertTrue(sudoku.is_solved())

    def test_multiple_basic_subgrid_solve(self):
        tiles = [
            [0, 3, 4, 0, 7, 8, 0, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [0, 5, 9, 0, 6, 1, 0, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [0, 6, 1, 0, 3, 7, 0, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        sudoku = Sudoku(tiles)
        solver = Solver(sudoku)
        solver.solve()
        self.assertTrue(sudoku.is_solved())

    

    def test_fully_solve_basic_sudoku(self):
        tiles = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        sudoku = Sudoku(tiles)
        solver = Solver(sudoku)
        solver.solve()
        self.assertTrue(sudoku.is_solved())

    def test_fully_solve_intermediate_sudoku(self):
        tiles = [
            [3, 0, 0, 0, 2, 8, 0, 6, 0],
            [0, 8, 5, 0, 6, 0, 4, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 7, 0],
            [0, 0, 7, 0, 0, 0, 6, 0, 0],
            [6, 4, 0, 8, 0, 1, 0, 0, 0],
            [5, 3, 0, 0, 7, 2, 0, 8, 0],
            [0, 0, 0, 1, 5, 7, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 9, 0],
            [0, 0, 0, 3, 0, 0, 0, 4, 0]
        ]
        sudoku = Sudoku(tiles)
        solver = Solver(sudoku)
        solver.solve()
        self.assertTrue(sudoku.is_solved())



    # def test(self):
    #     tiles = [
    #         [5, 3, 4, 6, 7, 8, 9, 1, 2],
    #         [6, 7, 2, 1, 9, 5, 3, 4, 8],
    #         [1, 9, 8, 3, 4, 2, 5, 6, 7],
    #         [8, 5, 9, 7, 6, 1, 4, 2, 3],
    #         [4, 2, 6, 8, 5, 3, 7, 9, 1],
    #         [7, 1, 3, 9, 2, 4, 8, 5, 6],
    #         [9, 6, 1, 5, 3, 7, 2, 8, 4],
    #         [2, 8, 7, 4, 1, 9, 6, 3, 5],
    #         [3, 4, 5, 2, 8, 6, 1, 7, 9]
    #     ]
    #     sudoku = Sudoku(tiles)
    #     solver = Solver(sudoku)
    #     solver.solve()
    #     self.assertTrue(sudoku.is_solved())
    # 
    # test template

if __name__ == '__main__':
    unittest.main()
from sudoku_reader import SudokuReader
from solver import Solver

def get_solution(path):
    reader = SudokuReader(path)
    matrix = reader.image_to_matrix()
    solver = Solver(matrix)
    solution = solver.get_solution()
    return solution



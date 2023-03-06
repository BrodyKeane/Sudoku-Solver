from sudoku_reader import SudokuReader
from solver import Solver

def main(path):
    reader = SudokuReader(path)
    matrix = reader.image_to_matrix()
    solver = Solver(matrix)
    return solver.get_solution()

path = 'images/s1.PNG'

if __name__ == "__main__":
    main(path)


class Solver:
    def __init__(self, sudoku) -> None:
        self.sudoku = sudoku
        self.progress_made = False

    def solve(self):
        while not self.sudoku.is_solved():
            self.progress_made = False
            self.solve_rows()
            self.solve_cols()
            self.solve_subgrids()
            if not self.progress_made:
                print(self.sudoku)
                print('Failed to solve puzzle')
                break
                

    def solve_rows(self):
        for row in range(9):
            group = self.sudoku.get_row(row)
            self.solve_group(group)

    def solve_cols(self):
        for col in range(9):
            group = self.sudoku.get_col(col)
            self.solve_group(group)

    def solve_subgrids(self):
        for subgrid in range(1,10):
            group = self.sudoku.get_subgrid_from_id(subgrid)
            self.solve_group(group)

    def solve_group(self, group):
        solved = set()

        for tile in group:
            solved.add(tile.value)

        for tile in group:
            if not tile.is_solved():
                tile.discard_values(solved)
                self.solve_tile(tile)

    def solve_tile(self, tile):
        if len(tile.possible_values) == 1:
            tile.value = tile.possible_values.pop()
            self.progress_made = True

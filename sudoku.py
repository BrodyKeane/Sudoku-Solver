class Tile:
    def __init__(self, value=0):
        self.value = value
        self.possible_values = {i for i in range(1, 10)}
        self.priority = len(self.possible_values)

    def discard_values(self, values):
        for val in values:
            self.possible_values.discard(val)

    def is_solved(self):
        return self.value != 0

    def __str__(self):
        return str(self.value)



class Sudoku:
    def __init__(self, values):
        self.tiles = [[Tile(value) for value in row] for row in values]

    def get_tile(self, row, col):
        return self.tiles[row][col]

    def set_tile(self, row, col, value):
        tile = self.get_tile(row, col)
        tile.value = value
        tile.possible_values = set()


    def get_row(self, row):
        return [self.get_tile(row, col) for col in range(9)]

    def get_col(self, col):
        return [self.get_tile(row, col) for row in range(9)]


    def get_subgrid_from_id(self, id):
        '''
        id ranges from 1 to 9 in left --> right order
        '''
        id -= 1
        sub_row = id // 3
        sub_col = id % 3
        return self._get_subgrid(sub_row, sub_col)

    def get_subgrid_from_coords(self, row, col):
        sub_row = row // 3
        sub_col = col // 3
        return self._get_subgrid(sub_row, sub_col)

    def _get_subgrid(self, sub_row, sub_col):
        subgrid = []
        for i in range(sub_row * 3, sub_row * 3 + 3):
            for j in range(sub_col * 3, sub_col * 3 + 3):
                subgrid.append(self.get_tile(i, j))
        return subgrid


    def is_valid(self):
        for i in range(9):
            if not self.is_valid_group(self.get_row(i)):
                return False
            if not self.is_valid_group(self.get_col(i)):
                return False
            if not self.is_valid_group(self.get_subgrid_from_coords(i // 3 * 3, i % 3 * 3)):
                return False
        return True

    def is_valid_group(self, group):
        seen = set()
        for tile in group:
            if tile.is_solved:
                if tile.value in seen:
                    return False
                seen.add(tile.value)
        return True

    def is_solved(self):
        for row in range(9):
            for col in range(9):
                tile = self.get_tile(row, col)
                if not tile.is_solved:
                    return False
        return self.is_valid()



    def __str__(self):
        result = "\n"
        for row in range(9):
            if row % 3 == 0:
                result += "+-------+-------+-------+\n"
            for col in range(9):
                if col % 3 == 0:
                    result += "| "
                tile = self.get_tile(row, col)
                if tile.value == 0:
                    result += ". "
                else:
                    result += str(tile) + " "
            result += "|\n"
        result += "+-------+-------+-------+"
        return result

# puzzle = [
#     [0, 0, 0,  2, 6, 0,  7, 0, 1],
#     [6, 8, 0,  0, 7, 0,  0, 9, 0],
#     [1, 9, 0,  0, 0, 4,  5, 0, 0],

#     [8, 2, 0,  1, 0, 0,  0, 4, 0],
#     [0, 0, 4,  6, 0, 2,  9, 0, 0],
#     [0, 5, 0,  0, 0, 3,  0, 2, 8],

#     [0, 0, 9,  3, 0, 0,  0, 7, 4],
#     [0, 4, 0,  0, 5, 0,  0, 3, 6],
#     [7, 0, 3,  0, 1, 8,  0, 0, 0]
# ]
# sudoku = Sudoku(puzzle)
# print(sudoku)
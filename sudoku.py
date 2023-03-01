class Tile:
    def __init__(self, position, value=0):
        self.position = position
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
        self.tiles = []
        self.remaining = set()
        for i, row in enumerate(values):
            row_of_tiles = []
            for j, value in enumerate(row):
                tile = Tile((i, j), value)
                row_of_tiles.append(tile)
                if value == 0:
                    self.remaining.add(tile) 
            self.tiles.append(row_of_tiles)


    def get_matrix(self):
        return self.tiles

    def set_tile(self, tile, value):
        tile.value = value
        tile.possible_values = set()
        self.remaining.discard(tile)


    def get_row(self, row):
        return self.tiles[row]

    def get_col(self, col):
        return [row[col] for row in self.tiles]


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
                subgrid.append(self.tiles[i][j])
        return subgrid
    
    def get_tiles_by_priority(self):
        priority = sorted(self.remaining, key=lambda tile: tile.priority)
        return priority


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
        for row in self.tiles:
            for tile in row:
                if not tile.is_solved():
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
                tile = self.tiles[row][col]
                if tile.value == 0:
                    result += ". "
                else:
                    result += str(tile) + " "
            result += "|\n"
        result += "+-------+-------+-------+"
        return result

# tiles = [
#     [8, 2, 1, 5, 6, 7, 9, 3, 4],
#     [3, 9, 7, 4, 2, 1, 8, 5, 6],
#     [6, 4, 5, 9, 3, 8, 7, 1, 2],
#     [5, 7, 4, 8, 1, 6, 3, 2, 9],
#     [2, 1, 8, 3, 9, 4, 6, 7, 5],
#     [9, 3, 6, 7, 5, 2, 4, 8, 1],
#     [1, 8, 2, 6, 7, 9, 5, 4, 3],
#     [7, 6, 3, 1, 4, 5, 2, 9, 8],
#     [4, 5, 9, 2, 8, 3, 1, 6, 7]
# ]
# sudoku = Sudoku(tiles)
# print(sudoku.is_solved())
# print(sudoku)
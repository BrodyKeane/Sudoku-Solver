class Solver:
    def __init__(self, board):
        self.board = board
        self.length = len(board)
        self.width = len(board[0])

    def get_solution(self):
        print(self)
        self.solve()
        print(self)
        return self.board
    
    def solve(self):
        find = self.find_empty()
        if not find:
            return True

        row, col = find

        for i in range(1,10):
            if self.valid(i, (row, col)):
                self.board[row, col] = i

                if self.solve():
                    return True

                self.board[row, col] = 0

        return False
    
    def valid(self, num, pos):
        row, col = pos
        for i in range(self.width):
            if self.board[row, i] == num and col != i:
                return False
            
        for i in range(self.length):
            if self.board[i, col] == num and row != i:
                return False

        box_x = col // 3
        box_y = row // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.board[i, j] == num and (i,j) != pos:
                    return False
        return True

    def find_empty(self):
        for i in range(self.length):
            for j in range(self.width):
                if self.board[i, j] == 0:
                    return (i, j)  # row, col
        return None


    def __str__(self):
        result = "\n"
        for row in range(9):
            if row % 3 == 0:
                result += "+-------+-------+-------+\n"
            for col in range(9):
                if col % 3 == 0:
                    result += "| "
                tile = self.board[row][col]
                if tile == 0:
                    result += ". "
                else:
                    result += str(tile) + " "
            result += "|\n"
        result += "+-------+-------+-------+"
        return result
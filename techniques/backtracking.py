class NQueens:
    def __init__(self, n: int):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def print_board(self) -> None:
        for row in self.board:
            print(" ".join("x" if cell == 1 else "o" for cell in row))

    def is_safe(self, row: int, col: int) -> bool:
        # check row (left side)
        for j in range(col):
            if self.board[row][j] == 1:
                return False

        # upper-left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # lower-left diagonal
        i, j = row, col
        while i < self.n and j >= 0:
            if self.board[i][j] == 1:
                return False
            i += 1
            j -= 1
        return True

    def solve(self, col: int) -> bool:
        if col == self.n:
            return True
        for row in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                if self.solve(col + 1):
                    return True
                self.board[row][col] = 0  # backtrack
        return False

    def solve_n_queens(self) -> None:
        if self.solve(0):
            self.print_board()
        else:
            print("No solution exists.")



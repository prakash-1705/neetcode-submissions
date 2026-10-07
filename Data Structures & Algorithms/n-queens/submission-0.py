class Solution(object):
    def isSafe(self, board, row, col, n):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True
    def solve(self, board, row, n, result):
        if row == n:
            result.append(["".join(r) for r in board])
            return
        for col in range(n):
            if self.isSafe(board, row, col, n):
                board[row][col] = 'Q'
                self.solve(board, row + 1, n, result)
                board[row][col] = '.'
    def solveNQueens(self, n):
        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []
        self.solve(board, 0, n, result)
        return result
        
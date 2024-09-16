class Solution:
    def solveSudoku(self, board):
        self.solve(board)
    
    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if self.isValid(board, i, j, num):
                            board[i][j] = num
                            if self.solve(board):
                                return True
                            board[i][j] = '.'
                    return False
        return True
    
    def isValid(self, board, row, col, num):
        # Check the row
        for i in range(9):
            if board[row][i] == num:
                return False
        
        # Check the column
        for i in range(9):
            if board[i][col] == num:
                return False
        
        # Check the 3x3 sub-box
        boxRow = (row // 3) * 3
        boxCol = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[boxRow + i][boxCol + j] == num:
                    return False
        
        return True

# Example Usage
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

solution = Solution()
solution.solveSudoku(board)
print(board)

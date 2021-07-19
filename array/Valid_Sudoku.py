class Solution(object):
    def isValidSudoku(self, board):
        return self.rowisValid(board)

    def rowisValid(self, board):
        n=len(board)
        for i in range(n):
            rownum = [x for x in board[i] if x != "."]
        
            if len(set(rownum))!=len(rownum):
                return False
        return True

    def columnisValid(self, board):
        n=len(board)
        for i in range(n):
            rownum = [board[j][i] for j in range(n) if board[j][i] != "."]
            if len(set(rownum))!=len(rownum):
                return False
        return True
    
    def isValidNineCell(self, board):
        n = len(board)
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                cell = []
                for k in range(3):
                    for l in range(3):
                        num = board[i + k][j + l]
                        if num != '.':
                            cell.append(num)
                if len(set(cell)) != len(cell):
                    return False
        return True


board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

s=Solution()
print(s.isValidNineCell(board))
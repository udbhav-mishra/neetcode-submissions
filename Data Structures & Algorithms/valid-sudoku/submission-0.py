class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                elif board[i][j] in check: return False
                else: check.add(board[i][j])
            check.clear()
        
        for i in range(9):
            for j in range(9):
                if board[j][i] == ".": continue
                elif board[j][i] in check: return False
                else: check.add(board[j][i])
            check.clear()

        for i in range(0 ,9 , 3):
            for j in range(0, 9, 3):
                for x in range(3):
                    for y in range(3):
                        if board[i + x][j + y] == ".": continue
                        elif board[i + x][j + y] in check: return False
                        else: check.add(board[i + x][j + y])
                check.clear()
        
        return True
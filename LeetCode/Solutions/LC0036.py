class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict={}   
        for i in board:
            for j in i:
                if j not in rowDict:
                    rowDict[j] = None
                elif j != ".":
                    return False
                # print(j)
            rowDict={}
        colDict={}
        for j in range(len(board)):
            for k in range(len(board)):
                if board[k][j] not in colDict:
                    colDict[board[k][j]] = None
                elif board[k][j] != ".":
                    return False
            colDict={}
        squareIn = 0
        squareOut = 0
        boxDict={}
        while squareOut < 9:
            while squareIn < 9:
                for i in range(3):
                    for j in range(3):
                        if board[squareOut+i][squareIn+j] not in boxDict:
                            boxDict[board[squareOut+i][squareIn+j]] = None
                        elif board[squareOut+i][squareIn+j] != ".":
                            return False
                boxDict={}
                squareIn += 3
            squareIn = 0
            squareOut += 3
        
            
        return True
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowDict,colDict,boxDict = {i:set() for i in range(9)},{i:set() for i in range(9)},{i:set() for i in range(9)}
        dotList = []
        #Populate dicts with row column and box entries
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    board[i][j] = int(board[i][j])
                    rowDict[i].add(board[i][j]) #Add to rows
                    colDict[j].add(board[i][j]) #Add to columns
                    #Add to boxes
                    if i < 3:
                        if j < 3:
                            boxDict[0].add(board[i][j])
                        elif j < 6:
                            boxDict[1].add(board[i][j])
                        elif j < 9:
                            boxDict[2].add(board[i][j])
                    elif i < 6:
                        if j < 3:
                            boxDict[3].add(board[i][j])
                        elif j < 6:
                            boxDict[4].add(board[i][j])
                        elif j < 9:
                            boxDict[5].add(board[i][j])
                    elif i < 9:
                        if j < 3:
                            boxDict[6].add(board[i][j])
                        elif j < 6:
                            boxDict[7].add(board[i][j])
                        elif j < 9:
                            boxDict[8].add(board[i][j])
                else:
                    board[i][j] = 0
                    if i < 3:
                        if j < 3:
                            dotList.append((i,j,0))
                        elif j < 6:
                            dotList.append((i,j,1))
                        elif j < 9:
                            dotList.append((i,j,2))
                    elif i < 6:
                        if j < 3:
                            dotList.append((i,j,3))
                        elif j < 6:
                            dotList.append((i,j,4))
                        elif j < 9:
                            dotList.append((i,j,5))
                    elif i < 9:
                        if j < 3:
                            dotList.append((i,j,6))
                        elif j < 6:
                            dotList.append((i,j,7))
                        elif j < 9:
                            dotList.append((i,j,8))
        def backtrack(dot,backwards):
            currentNum = board[dotList[dot][0]][dotList[dot][1]]
            if backwards:
                rowDict[dotList[dot][0]].remove(currentNum)
                colDict[dotList[dot][1]].remove(currentNum)
                boxDict[dotList[dot][2]].remove(currentNum)
            if currentNum < 9:
                board[dotList[dot][0]][dotList[dot][1]] += 1
                currentNum += 1
                if currentNum in rowDict[dotList[dot][0]] or currentNum in colDict[dotList[dot][1]] or currentNum in boxDict[dotList[dot][2]]:
                    backtrack(dot,False)
                elif dot < len(dotList)-1:
                    rowDict[dotList[dot][0]].add(currentNum)
                    colDict[dotList[dot][1]].add(currentNum)
                    boxDict[dotList[dot][2]].add(currentNum)
                    backtrack(dot+1,False)
                else:
                    return
            else:
                board[dotList[dot][0]][dotList[dot][1]] = 0
                backtrack(dot-1,True)
        backtrack(0,False)
        for i in range(9):
            for j in range(9):
                board[i][j] = str(board[i][j])
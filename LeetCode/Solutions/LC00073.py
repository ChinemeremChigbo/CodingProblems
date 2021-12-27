class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowSet = set()
        colSet = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rowSet or j in colSet:
                    matrix[i][j] = 0

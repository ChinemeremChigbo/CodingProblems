class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        right,down,left,up,i,j,count = True,False,False,False,0,0,1
        while count <= n*n:
            if right:
                matrix[i][j] = count
                if j + 1 < n and matrix[i][j+1] == 0: j += 1
                else: i, right,down = i+1,False,True
            elif down:
                matrix[i][j] = count
                if i + 1 < n and matrix[i+1][j] == 0: i += 1
                else: j,down,left = j-1,False,True
            elif left:
                matrix[i][j] = count
                if j - 1 > -1 and matrix[i][j-1] == 0: j -= 1
                else: i,left,up = i-1,False,True
            elif up:
                matrix[i][j] = count
                if i - 1 > -1 and matrix[i-1][j] == 0: i -= 1
                else: j,up,right = j+1,False,True
            count += 1
        return matrix
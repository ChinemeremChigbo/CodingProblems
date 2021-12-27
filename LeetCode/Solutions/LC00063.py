class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for i,row in enumerate(obstacleGrid):
            for j,num in enumerate(row):
                if num == 1: obstacleGrid[i][j] = 0
                elif i == 0 and j == 0: obstacleGrid[i][j] = 1
                elif i == 0: obstacleGrid[i][j] = obstacleGrid[i][j-1]
                elif j == 0: obstacleGrid[i][j] = obstacleGrid[i-1][j]
                else: obstacleGrid[i][j] = obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]
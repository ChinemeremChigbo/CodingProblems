class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        newList = [val for row in matrix for val in row]
        return target in newList
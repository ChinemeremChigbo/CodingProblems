class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        r = g = b = 0
        for num in nums:
            if num == 0:
                r += 1
            elif num == 1:
                g += 1
            else:
                b += 1
        nums[:] = [0]*r + [1]*g + [2]*b
        
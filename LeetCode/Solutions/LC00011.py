class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPointer = 0
        rightPointer = len(height)-1
        maxArea = 0
        while rightPointer - leftPointer > 0:
            maxArea = max(maxArea,(rightPointer-leftPointer)*min(height[rightPointer],height[leftPointer]))
            if  height[leftPointer] < height[rightPointer]:
                leftPointer += 1
            else:
                rightPointer -= 1
        return maxArea
        
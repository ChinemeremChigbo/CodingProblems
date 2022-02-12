class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0;
        size = len(height)
        if size <= 2:
            return 0
        leftMax = [0] * size 
        rightMax = [0] * size
        leftMax[0] = height[0]        
        for i in range(1, size):
            leftMax[i] = max(height[i], leftMax[i-1])
        rightMax[size-1] = height[size-1]
        for j in reversed(range(0, size-1)):
            rightMax[j] = max(height[j], rightMax[j+1])
        for k in range(1, size - 1):
            ans += min(leftMax[k], rightMax[k]) - height[k]
        return ans;
                

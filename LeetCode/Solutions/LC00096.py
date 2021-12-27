class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0],dp[1] = 1,1
        for i in range(2,n + 1):
            for left in range(i):
                right = i - 1 - left
                dp[i] += dp[left] * dp[right]
        return dp[-1]
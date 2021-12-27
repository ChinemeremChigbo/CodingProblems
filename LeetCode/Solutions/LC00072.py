class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0 if j!=0 and i!=0 else j if j!= 0 else i for i in range(n+1)] for j in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = min([dp[i-1][j],dp[i-1][j-1],dp[i][j-1]]) + 1 if word2[i-1]!= word1[j-1] else dp[i-1][j-1]
        return dp[-1][-1]
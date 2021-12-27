class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1:1,2:2}
        def climb(n):
            if n in cache:
                return cache[n]
            result = climb(n-1) + climb(n-2)
            cache[n] = result
            return result
        return climb(n)
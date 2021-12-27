class Solution:
    def mySqrt(self, x: int) -> int:
        def binary(x):
            left = 0
            right = 46341
            while left < right:
                mid = (left + right) // 2
                if (mid * mid) > x:
                    right = mid
                else:
                    left = mid + 1
            return left
        res = binary(x)
        return res if (res * res) < x else res - 1
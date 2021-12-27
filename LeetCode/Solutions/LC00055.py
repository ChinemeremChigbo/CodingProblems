class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        def jumpable(index):
            for i in range(index-1, -1, -1):
                if nums[i]+i > index:
                    return True
            return False
        while i < n-1:
            if nums[i] == 0:
                if not jumpable(i):
                    return False
                i += 1
            i += nums[i]
        return True
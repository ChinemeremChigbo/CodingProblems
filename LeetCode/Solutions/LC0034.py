class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def bisect_left(nums,target,cool):
            lo = 0
            hi = n
            mid = (lo + hi) // 2
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo if not cool else mid
        lo = bisect_left(nums,target,False)
        return [lo, bisect.bisect(nums, target,True)-1] if target in nums[lo:lo+1] else [-1, -1]
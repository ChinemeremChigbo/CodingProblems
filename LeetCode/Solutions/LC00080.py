class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 1
        p3 = 2
        while p3 < len(nums):
            if nums[p1] == nums[p2] == nums[p3]:
                nums.pop(p3)
            else:
                p1,p2,p3 = p2,p3,p3+1
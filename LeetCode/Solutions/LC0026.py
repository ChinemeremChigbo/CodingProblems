class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = inf
        nums.sort()
        for j in range(len(nums)):
            if nums[j] == inf:
                return j
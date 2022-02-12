class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(sorted(set(nums)))
        counter = 0
        for i in nums:
            if i > 0:
                counter +=1
                if counter != i:
                    return counter
        if nums[len(nums)-1] > 0:
            return (nums[len(nums)-1]+1)
        return 1
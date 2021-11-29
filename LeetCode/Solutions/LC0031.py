class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        popped = []
        for i in reversed(nums):
            if popped and popped[-1] > nums[-1]:
                insert = bisect.bisect(popped,(nums[-1]))
                num = nums.pop(-1)
                nums.append(popped.pop(insert))
                bisect.insort(popped,num)
                nums += (popped)
                return
            bisect.insort(popped,(nums.pop(-1)))
        nums[:] = popped

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        finalList = []
        for i in range(2**len(nums)):
            listEntry = sorted([nums[j] for j in range(len(nums)) if ('{:0>10}'.format(str(bin(i))[2:])[::-1][j]) == "1" ])
            if listEntry not in finalList:
                finalList += [listEntry]
        return finalList
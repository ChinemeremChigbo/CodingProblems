class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n > 2:
            solutions = set()
            seen = set()
            nums.sort()
            if nums.count(0) > 2:
                solutions.add((0,0,0))
            for i in range(n):
                for j in range(i+1,n):
                    ni, nj = nums[i], nums[j]
                    if ni == 0 and nj == 0:
                        continue
                    complement = -(ni+nj)
                    if complement in seen:
                        solutions.add((ni,nj,complement))
                seen.add(ni)
            return solutions
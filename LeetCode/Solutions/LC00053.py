class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pointer1 = pointer2 = 0
        maxSoFar = currentSum = nums[0]
        n = len(nums)
        while pointer2 < n:
            maxSoFar = max(maxSoFar,currentSum)
            if pointer2 < n - 1:
                afterp2 = nums[pointer2+1]
                if afterp2 > currentSum+afterp2: #Start Afresh
                    currentSum = afterp2
                    pointer1 = pointer2 + 1
                else: #Extend
                    currentSum += afterp2
            pointer2 += 1
        return maxSoFar
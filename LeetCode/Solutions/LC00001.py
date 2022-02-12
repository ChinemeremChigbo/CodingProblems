'''
Solution

There isn't too much I can add to the discussion of this classic leetcode question.
In order to get two numbers that sum to the target we must add the current number with target - num
So for each number we store it's complement in the dictionary and if we come across a number that has
been added to the dictionary we know that it's complement must also have been seen before.

Complexity

Time - O(n): We iterate over each number at least once
Space - O(n): The dictionary stores at most n elements (where n is the length of nums)

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i, num in enumerate(nums):
            if num in differences:
                return(i,differences[num])
            differences[target - num] = i

        
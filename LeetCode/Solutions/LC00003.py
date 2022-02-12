class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = {}
        leftWindow = 0
        maxWindow = 0
        for i, ins in enumerate(s):
            if ins not in charDict:
                charDict[ins] = i
            else:
                x = charDict[ins]
                if x + 1 > leftWindow:
                    leftWindow = x + 1
                charDict[ins] = i
            maxWindow = max(maxWindow,i-leftWindow+1)
            
        return maxWindow
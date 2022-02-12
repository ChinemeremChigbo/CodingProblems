class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        maxSubstring = (s[0],1)
        def centerExpansion(start,end):
            while start > -1 and end < length and s[start] == s[end]:
                start -= 1
                end += 1
            return (s[start+1:end],end-start-1)
        for i in range(length - 1):
            a = centerExpansion(i,i)
            b = centerExpansion(i,i+1)
            longer = a if a[1] > b[1] else b
            maxSubstring = longer if longer[1] > maxSubstring[1] else maxSubstring
        return maxSubstring[0]

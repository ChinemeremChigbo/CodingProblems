class Solution:
    def isPalindrome(self, x: int) -> bool:
        return (a:=str(x)) == a[::-1]
        
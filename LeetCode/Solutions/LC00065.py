class Solution:
    def isNumber(self, s: str) -> bool:
        if "inf" in s.lower():
            return False
        try:
            (float(s))
            return True
        except:
            return False
        
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(re.sub("\s+"," ",s).strip().split(" ")[-1])
import re
from functools import lru_cache  
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.match("^{}$".format(p), s)
    @lru_cache()
    def isMatch(self, text: str, pattern: str) -> bool:
        if not pattern:
            return not text

        first = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first and self.isMatch(text[1:], pattern))
        else:
            return first and self.isMatch(text[1:], pattern[1:])
class Solution:
    def countAndSay(self, n: int) -> str:
        seen = {}
        def split(s):
            splitted = []
            p1 = 0
            p2 = 0
            while p2 < len(s):
                if s[p1] != s[p2]:
                    splitted.append(s[p1:p2])
                    p1 = p2
                p2 += 1
            if p1!=p2:
                splitted.append(s[p1:p2+1])
            return splitted
        def say(word, count):
            if count == n:
                return word
            nextN = ""
            for sub in split(word):
                if sub in seen:
                    nextN += seen[sub]
                else:
                    subNext = str(len(sub))+sub[0]
                    nextN+=(subNext)
                    seen[sub] = subNext
            return say(nextN,count+1)
        return say("1",1)
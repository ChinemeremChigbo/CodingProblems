import random
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid( s: str) -> bool:
            stack=[]
            for p in s:
                if p in ["("]:
                    stack.append(p)
                else:
                    if not stack:
                        return False
                    x=stack.pop()
                    if x=='(':
                        if p!=")":
                            return False
            if stack:
                return False
            return True
        brackets = ""
        for i in range(n-1):
            brackets += "("
        for i in range(n-1):
            brackets += ")"   
        bracketList = []
        count = 0
        while count < 470*pow(n,2):
            if isValid("("+brackets+")") and "("+brackets+")" not in bracketList:
                bracketList += ["("+brackets+")"]
            l = list(brackets)
            random.shuffle(l)
            brackets = ''.join(l)
            count += 1
        return (bracketList)

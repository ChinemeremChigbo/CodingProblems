class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for p in s:
            if p in ["(","[","{"]:
                stack.append(p)
            else:
                if not stack:
                    return False
                x=stack.pop()
                if (x=='(' and p!=")") or (x=='['and p!="]") or (x=='{' and p!="}"):
                        return False 
        if stack:
            return False
        return True
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        validNumber = {str(n) for n in range(256)}
        finalList = []
        for i in range(1,4):
            for j in range(1,4):
                for k in range(1,4):
                    for l in range(1,4):
                        if i+j+k+l == len(s):
                            if s[0:i] in validNumber and s[i:i+j] in validNumber and s[i+j:i+j+k] in validNumber and s[i+j+k:] in validNumber:
                                finalList += [s[0:i]+"."+s[i:i+j]+"."+s[i+j:i+j+k]+"."+s[i+j+k:]]
        return finalList
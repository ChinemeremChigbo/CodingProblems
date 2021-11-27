class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numDict = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        if not(digits): return []
        n = len(digits)
        if n == 1: return numDict[digits[0]]
        res = []
        #When digits.length == 2
        if len(digits) == 2:
            for i in numDict[digits[0]]:
                for j in numDict[digits[1]]:
                    res.append(i+j)
        #When digits.length == 3
        elif len(digits) == 3:
            for i in numDict[digits[0]]:
                for j in numDict[digits[1]]:
                    for k in numDict[digits[2]]:
                        res.append(i+j+k)
        #When digits.length == 4
        elif len(digits) == 4:
            for i in numDict[digits[0]]:
                for j in numDict[digits[1]]:
                    for k in numDict[digits[2]]:
                        for l in numDict[digits[3]]:
                            res.append(i+j+k+l)
        return res
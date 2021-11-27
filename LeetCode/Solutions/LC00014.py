class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        sCount = 0
        lCount = 0
        outerLength = len(strs)
        firstLetter = True
        while True:
            try:
                strs[sCount][lCount]
            except:
                break
            if firstLetter == False and sCount!=0:
                if previousLetter != strs[sCount][lCount]:
                    break
            previousLetter = strs[sCount][lCount]
            if sCount == outerLength - 1:
                prefix += strs[sCount][lCount]
            firstLetter = False
            sCount+=1
            if (sCount) == outerLength:
                sCount = 0
                lCount += 1
        return prefix
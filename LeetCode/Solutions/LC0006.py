class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rowArray = []
        strList = list(s)
        for i in range(numRows):
            rowArray.append([])
        i = 0
        direction = 1
        while strList != []:
            rowArray[i].append(strList.pop(0))
            i+=direction
            if i == len(rowArray)-1:
                direction = -1
            if i == 0:
                direction = 1
        finalList = ""
        for i in rowArray:
            for j in i:
                finalList += j
        return(finalList)
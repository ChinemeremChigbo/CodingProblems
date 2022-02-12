class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        numString = str(num)
        # length = len(numString)
        i1 = {"1":"I","2":"II","3":"III","4":"IV","5":"V","6":"VI","7":"VII","8":"VIII","9":"IX"}
        i2 = {"1":"X","2":"XX","3":"XXX","4":"XL","5":"L","6":"LX","7":"LXX","8":"LXXX","9":"XC"}
        i3 = {"1":"C","2":"CC","3":"CCC","4":"CD","5":"D","6":"DC","7":"DCC","8":"DCCC","9":"CM"}
        i4 = {"1":"M","2":"MM","3":"MMM"}
        for i in range(len(numString)):
            if numString[i] == "0":
                continue
            if i == len(numString)-1:
                result += i1[numString[i]]
            elif i == len(numString)-2:
                result += i2[numString[i]]
            elif i == len(numString)-3:
                result += i3[numString[i]]
            else:
                result += i4[numString[i]]
        return result

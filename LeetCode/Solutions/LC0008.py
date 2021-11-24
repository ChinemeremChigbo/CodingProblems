class Solution:
    def myAtoi(self, s: str) -> int:
        numToParse = ""
        allowedDict = {" ":"","-":"-","+":"+","0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}
        allowedDict2 = {"-":"-","+":"+","0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}
        num = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        signChange = False
        for i in range(len(s)):
            if s[i] in allowedDict:
                if s[i] == "+" and signChange == True:
                    break
                if s[i] == "-" and signChange == True:
                    break
                if s[i] == " " and signChange == True:
                    break
                if s[i] in allowedDict2:
                    signChange = True
                numToParse+=allowedDict[s[i]]
            else: break
        if numToParse == "":
            return 0
        else:
            try:
                solution = int(numToParse)
                if solution > 2147483647:
                    return 2147483647
                elif solution < -2147483648:
                    return -2147483648
                return solution
            except:
                return 0
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        if num1 == "1":
            return num2
        if num2 == "1":
            return num1
        number1 = 0
        number2 = 0
        numDict = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        for i in reversed(range(len(num1))):
            number1+=numDict[num1[i]]*(pow(10,len(num1)-1-i))
        for j in reversed(range(len(num2))):
            number2+=numDict[num2[j]]*(pow(10,len(num2)-1-j))
        return(str(number1 * number2))
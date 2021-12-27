class Solution:
    def grayCode(self, n: int) -> List[int]:
        finalList= []
        for i in range(pow(2,n)):
            newNumber = ""
            binary = str(bin(i))[2:]
            for j in range(len(binary)):
                    if j == 0:
                        newNumber+=(binary[j])
                    else:
                        newNumber+=(str(int((binary[j])!=(binary[j-1]))))
            finalList += [(int(newNumber,2))]
        return finalList
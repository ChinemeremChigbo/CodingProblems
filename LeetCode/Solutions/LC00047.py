class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        uniqueList = []
        entryDict = {}
        counter = 0
        dictCounter = 0
        maxTimeout = pow(4,len(nums))
        while len(uniqueList) < math.factorial(len(nums)) and counter < maxTimeout:
            shuffledNums = sorted(nums, key = lambda x: random.random())
            if str(shuffledNums) not in entryDict:
                entryDict[str(shuffledNums)] = dictCounter
                dictCounter += 1
                uniqueList += [shuffledNums]
            counter += 1
        return(uniqueList)
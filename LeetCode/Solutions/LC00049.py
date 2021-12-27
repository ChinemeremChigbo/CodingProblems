class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = []
        wordSortedDict = {}
        counter = 0
        for i in strs:
            k =  str(sorted(i))
            if k not in wordSortedDict:
                wordSortedDict[k] = [i, counter]
                strings += [[i]]
                counter += 1
            else:
                strings[(wordSortedDict[k][1])]+=[i]
        return(strings)
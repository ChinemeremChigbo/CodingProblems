class Solution:
    def numDecodings(self, s: str) -> int:
        def helperFunc(data,k, memoized):
            if k == 0:
                return 1
            startingIndex = len(data) - k
            result = helperFunc(data, k - 1, memoized)
            if data[startingIndex] == '0':
                return 0
            if memoized[k] != None:
                return memoized[k]
            if k >=2 and int(data[startingIndex:startingIndex+2]) <= 26:
                result += helperFunc(data, k-2, memoized)
            memoized[k] = result
            return result
        memoized = [None for i in range(len(s) + 1)]
        return helperFunc(s, len(s), memoized)    
    
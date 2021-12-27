class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        idx = 0
        startLength = len(intervals)
        while idx < len(intervals) - 1:
            curr = intervals[idx]
            nxt = intervals[idx+1]
            if curr[1] >= nxt[0]:
                curr[0] = min(curr[0],nxt[0])
                curr[1] = max(curr[1],nxt[1])
                intervals.pop(idx+1)
            idx += 1
        endLength = len(intervals)
        
        if startLength == endLength:
            return intervals
        else:
            return(self.merge(intervals))
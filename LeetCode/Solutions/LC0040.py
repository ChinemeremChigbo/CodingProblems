class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(remain,curr,results):
        
            if remain == 0:
                results.append(combList[:])
                return

            for next_curr in range(curr, len(candidates)):
                if next_curr > curr and candidates[next_curr] == candidates[next_curr-1]:
                    continue
                pick = candidates[next_curr]
                if remain - pick < 0:
                    break

                combList.append(pick)
                backtrack(remain - pick, next_curr + 1, results)
                combList.pop()
        candidates.sort()
        combList, results = [], []
        backtrack(target, 0, results)

        return results
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(total,index,currentList):
            if total > target:
                return
            if total == target:
                print(total,currentList)
                result.append(currentList[:])
                return
            else:
                for i in range(index, len(candidates)):
                    currentList.append(candidates[i])
                    backtrack(sum(currentList), i, currentList)
                    currentList.pop()
                
        backtrack(0,0,[])
        return result

        
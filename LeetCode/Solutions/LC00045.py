class Solution:
    def jump(self, nums: List[int]) -> int:
        self.count = 0
        nums = list(enumerate(nums))
        n = len(nums)
        visited = set()
        def bfs(nodeList):
            while nodeList:
                newNodeList = set()                
                for pos, num in nodeList:
                    if pos == n - 1:
                        return self.count
                    if pos not in visited:
                        visited.add(pos)
                        newNodeList.update([i for i in nums[pos+1:pos+num+1]])
                nodeList = newNodeList
                self.count += 1
        return bfs({nums[0]})
    
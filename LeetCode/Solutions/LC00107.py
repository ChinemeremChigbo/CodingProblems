# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        bfs = [root]
        res = []
        while bfs:
            nextList = []
            res.append([i.val for i in bfs])
            for node in bfs:
                if node.left:
                    nextList.append(node.left)
                if node.right:
                    nextList.append(node.right)
            bfs = nextList
        return res[::-1]
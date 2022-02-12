# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        bfs = [root]
        while bfs:
            newBfs = []
            for node in bfs:
                if node:
                    newBfs.append(node.left)
                    newBfs.append(node.right)
            bfs = newBfs
            if [node.val if node else None for node in bfs]!=[node.val if node else None for node in bfs][::-1]:
                return False
        return True
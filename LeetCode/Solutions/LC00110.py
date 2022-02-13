# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        mem = {}
        def dfs(root):
            if not root: mem[root] = (0,0)
            elif root.left and  root.right:
                mem[root] = (1 + max(dfs(root.left)), 1 + max(dfs(root.right)))
            elif root.left:
                mem[root] = (1 + max(dfs(root.left)),0)
            elif root.right:
                mem[root] = (0,1 + max(dfs(root.right)))
            else:
                mem[root] = (0,0)
            return mem[root]
        dfs(root)
        for a,b in mem.values():
            if abs(a-b) > 1:
                return False
        return True
 
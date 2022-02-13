# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root == None: return False
        if root.val == targetSum and root.left == None == root.right: return True
        right, left = self.hasPathSum(root.left,targetSum - root.val), self.hasPathSum(root.right, targetSum - root.val)        
        return right or left
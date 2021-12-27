# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, maxVal, minVal):
            if not root:
                return True 
            
            if root.val <= minVal or root.val >= maxVal:
                return False 
            
            left = validate(root.left, root.val, minVal)
            right = validate(root.right, maxVal, root.val)
            
            return left and right 
        
        return validate(root, float('inf'), float('-inf'))
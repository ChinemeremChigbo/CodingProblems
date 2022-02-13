# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def recurse(inorder,preorder):
            root = TreeNode(preorder[0])
            rootPos = inorder.index(preorder[0])
            left = inorder[:rootPos]
            right = inorder[rootPos + 1:]
            if left:
                root.left = recurse(left,preorder[1:1+len(left)])
            if right:
                root.right = recurse(right,preorder[1 + len(left) : 1 + len(left) + len(right)])
            return root
        return recurse(inorder,preorder)
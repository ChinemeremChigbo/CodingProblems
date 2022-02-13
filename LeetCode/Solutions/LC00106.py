# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder = left, root, right
        # postorder = left, right, root
        def recurse(inorder,postorder):
            root = TreeNode(postorder[-1])
            rootPos = inorder.index(postorder[-1])
            left = inorder[:rootPos]
            right = inorder[rootPos + 1:]
            if left:
                root.left = recurse(left,postorder[:len(left)])
            if right:
                root.right = recurse(right,postorder[len(left) :len(left) + len(right)])
            return root
        return recurse(inorder,postorder)
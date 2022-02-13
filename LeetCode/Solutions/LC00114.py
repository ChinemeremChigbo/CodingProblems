# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return
        self.nodeList = []
        def preorder(root):
            if root:
                self.nodeList.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        root.left,root.right = None, None
        for num in self.nodeList[1:]:
            root.right = TreeNode(num)
            root = root.right    
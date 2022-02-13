# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        nodeList = {root}
        depth = 0
        while nodeList:
            newNodeList = set()
            for node in nodeList:
                if node:
                    if (node.left):
                        newNodeList.add(node.left)
                    if (node.right):
                        newNodeList.add(node.right)
                else:
                    return 0
            nodeList = newNodeList
            depth += 1
        return depth
                
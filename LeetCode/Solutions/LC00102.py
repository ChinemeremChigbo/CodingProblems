# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeList = [root] if root else []
        finalList = []
        while nodeList:
            finalList.append([node.val for node in nodeList])
            newList = []
            for i in nodeList:
                if i:
                    if i.left:
                        newList.append(i.left)
                    if i.right:
                        newList.append(i.right)
            nodeList = newList
        return finalList
            
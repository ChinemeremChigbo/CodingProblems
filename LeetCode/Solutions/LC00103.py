# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeList = [root] if root else []
        finalList = []
        count = 0
        while nodeList:
            newList = []
            if count%2 == 0:
                finalList.append([i.val for i in (nodeList)])
            else:
                finalList.append([i.val for i in reversed(nodeList)])
            for i in nodeList:
                if i.left:
                    newList.append(i.left)
                if i.right:
                    newList.append(i.right)
            count += 1
            nodeList = newList
        return finalList
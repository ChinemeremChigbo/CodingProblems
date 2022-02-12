# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def checkTree(p: TreeNode, q: TreeNode, nodeList1, nodeList2) -> bool:
            for i in range(len(nodeList1)):
                try:
                    if nodeList1[i]:
                        if nodeList1[i].val != nodeList2[i].val:
                            return False
                    if nodeList2[i]:
                        if nodeList1[i].val != nodeList2[i].val:
                            return False
                except:
                    return False
            newNodeList1 = []
            newNodeList2 = []
            for i in nodeList1:
                if i:
                    newNodeList1 += [i.left]
                    newNodeList1 += [i.right]
            for i in nodeList2:
                if i:
                    newNodeList2 += [i.left]
                    newNodeList2 += [i.right]
            nodeList1 = newNodeList1
            nodeList2 = newNodeList2
            if not nodeList1 and not nodeList2:
                return True
            return checkTree(p,q,nodeList1,nodeList2)
        return checkTree(p,q,[p],[q])
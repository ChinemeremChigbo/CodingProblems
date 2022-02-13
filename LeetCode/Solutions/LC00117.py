"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        bfsList = [root]
        while bfsList:
            newList = []
            n = len(bfsList)
            for i,node in enumerate(bfsList):
                if i+1 < n: bfsList[i].next =  bfsList[i+1]
                if node.left: newList.append(node.left)
                if node.right: newList.append(node.right)
            bfsList = newList
        return root
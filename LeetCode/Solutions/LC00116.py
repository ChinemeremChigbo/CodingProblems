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
        def bfs(nodeList):
            while nodeList:
                newNodeList = []
                for i, node in enumerate(nodeList):
                    if node:
                        if i < len(nodeList) - 1:
                            node.next = nodeList[i+1]
                        newNodeList.append(node.left)
                        newNodeList.append(node.right)
                nodeList = newNodeList
        bfs([root])
        return root
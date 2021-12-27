# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def checkBfs(nodeList, target, direction):
            rightMin = target
            leftMin = target
            while nodeList:
                newNodeList = []
                for i in nodeList:
                    if i:
                        if direction == "right" and i.val < rightMin:
                            rightMin = i.val
                            original = i
                        elif direction == "left" and i.val > leftMin:
                            leftMin = i.val
                            original = i
                        if i.left:
                            newNodeList.append(i.left)
                        if i.right:
                            newNodeList.append(i.right)
                nodeList = newNodeList
            if direction == "right":
                if rightMin != target:
                    return [original,rightMin]
                return None
            if direction == "left":
                if leftMin != target:
                    return [original,leftMin]
                return None
        nodeList = [root]
        rightSwitch = None
        leftSwitch = None
        while nodeList:
            newNodeList = []
            for i in nodeList:
                if i.right:
                    rightSwitch = checkBfs([i.right], i.val,"right")
                if i.left:
                    leftSwitch = checkBfs([i.left], i.val,"left")
                if rightSwitch and leftSwitch:
                    rightSwitch[0].val, leftSwitch[0].val = leftSwitch[1],rightSwitch[1]
                    return
                elif rightSwitch:
                    i.val,rightSwitch[0].val = rightSwitch[1],i.val
                    return
                elif leftSwitch:
                    i.val,leftSwitch[0].val = leftSwitch[1],i.val
                    return
                else:
                    if i.left:
                        newNodeList.append(i.left)
                    if i.right:
                        newNodeList.append(i.right)
            nodeList = newNodeList

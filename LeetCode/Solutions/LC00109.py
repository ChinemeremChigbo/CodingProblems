# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nodeList = []
        while head:
            nodeList.append(head.val)
            head = head.next
        def build(l,r):
            if l < r:
                m = (l+r) // 2
                root = ListNode(nodeList[m])
                root.left = build(l,m)
                root.right = build(m+1,r)
                return root
        return build(0,len(nodeList))
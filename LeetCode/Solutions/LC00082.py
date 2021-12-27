# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeVals = defaultdict(int)
        ptr = head
        while ptr:
            nodeVals[ptr.val] += 1
            ptr = ptr.next
        uniqueList = [i for i in nodeVals if nodeVals[i] == 1]
        res = tmp = ListNode(0)
        for el in uniqueList:
            tmp.next = ListNode(el)
            tmp = tmp.next
        return res.next
        

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pointer1 = head
        nodeList = []
        
        while pointer1 != None:
            nodeList += [pointer1.val]
            pointer1 = pointer1.next

        tempElement = 0
        for i in range(0, len(nodeList)-1, 2):
            tempElement = nodeList[i]
            nodeList[i] = nodeList[i+1]
            nodeList[i+1] = tempElement
        
        newHead = ListNode(0)
        iterator = newHead
        for i in nodeList:
            iterator.next = ListNode(i)
            iterator = iterator.next
            
        return newHead.next
        
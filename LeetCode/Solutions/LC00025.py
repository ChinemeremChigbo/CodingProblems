# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        reversedList = []
        kCounter = 1
        headCopy = head
        llist = []
        while headCopy != None:
            llist += [headCopy.val]
            headCopy = headCopy.next
            #Flip the digits and add them to a list
            if kCounter % k == 0:
                reversedList += llist[::-1]
                llist = []
            kCounter += 1
        #add the remaining digits
        reversedList += llist
        
        fakeHead = ListNode(None, None)
        newHead = fakeHead
        for i in reversedList:
            newHead.next = ListNode(i, None)
            newHead = newHead.next
        return(fakeHead.next)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        iterator1 = head
        iterator2 = head
        length = 2
        
        #Only 1 Element
        if head.next == None:
            return ListNode("", None)
        #Count Elements
        while iterator1.next.next != None:
            iterator1 = iterator1.next
            length += 1
            
        #Gets rid of ns at the end
        if n == length:
            return head.next
        
        #Gets rid of ns at the start
        elif n == 1:
            iterator1.next = None
            return head
        
        #Gets rid of ns in the middle 
        for i in range(length - n - 1):
            iterator2 = iterator2.next
        iterator2.next = iterator2.next.next
        return head
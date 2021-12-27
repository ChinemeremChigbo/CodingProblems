# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        iterator = head
        nodeList = []
        counter = 0
        while iterator != None:
            if counter >= left - 1 and counter <= right -1:
                nodeList.append(iterator.val)
            counter += 1
            iterator = iterator.next
        nodeList.reverse()            
        
        iterator = head
        counter = 0
        nodeListCounter = 0
        while iterator != None:
            if counter >= left - 1 and counter <= right -1:
                iterator.val = nodeList[nodeListCounter]
                nodeListCounter +=1
            counter += 1
            iterator = iterator.next
        return head
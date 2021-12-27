# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        nums = []
        while head != None:
            nums += [head.val]
            head = head.next
        if len(nums) == 0:
            return ListNode("")
        newArray = [0]*len(nums)
        k%=len(nums)
        for i in range(len(newArray)):
            newArray[i-(len(nums)-k)] = nums[i]
        newHead = ListNode(0)
        tmp = newHead
        
        for i in newArray:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return newHead.next
    
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ll = [[]]
        temp = head
        count = 0
        maxx = 1
        while temp:
            if count == maxx:
                maxx += 1
                count = 0
                ll.append([])
            count += 1
            ll[-1].append(temp.val)
            temp = temp.next
         
        final = []
        for i,group in enumerate(ll):
            if len(group) % 2 == 0:
                final.extend(group[::-1])
            else: final.extend(group)
                
        res = tmp = ListNode(0)
        for i in final:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return res.next
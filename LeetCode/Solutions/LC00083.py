# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = runner = head
        while node:
            if node.next and node.val == node.next.val:
                while runner.next and runner.val == runner.next.val:
                    runner = runner.next
                node.next = runner.next
            node, runner = node.next, runner.next
        return head
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            l3 = ListNode(0,None)
            pointer1 = l1
            pointer2 = l2
            iter3 = l3
            while pointer1 != None or pointer2 != None:
                if pointer1 == None:
                    iter3.next = pointer2
                    return l3.next
                elif pointer2 == None:
                    iter3.next = pointer1
                    return l3.next
                elif pointer1.val < pointer2.val:
                    iter3.next = ListNode(pointer1.val,None)
                    iter3 = iter3.next
                    pointer1 = pointer1.next
                else:
                    if pointer2 != None:
                        iter3.next = ListNode(pointer2.val,None)
                        iter3 = iter3.next
                        pointer2 = pointer2.next
            return l3.next
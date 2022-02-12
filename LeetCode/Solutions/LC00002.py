# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        listLength1,listLength2 = 0,0
        iter1,iter2 = l1, l2
        list1, list2, list3 = [], [], []
        while iter1:
            list1.append(iter1.val)
            iter1 = iter1.next
            listLength1 += 1
        while iter2:
            list2.append(iter2.val)
            iter2 = iter2.next
            listLength2 += 1
        if listLength1 < listLength2:
            l1, l2, list1, list2 = l2, l1, list2, list1
        list2.extend([0]*(len(list1)-len(list2)))
        carryOver = 0
        for i in range(len(list1)):
            list3.append(((list1[i]+list2[i])%10+carryOver) % 10)
            if (list1[i]+list2[i]+carryOver)>=10:
                carryOver = 1
            else:
                carryOver = 0   
        if (carryOver): list3.append(1)
        head = tmp = ListNode(0)
        for i in list3:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return head.next

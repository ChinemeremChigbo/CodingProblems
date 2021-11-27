# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodeList = []
        for i in lists:
            while i != None:
                nodeList.append(i.val)
                i = i.next
        if(nodeList == []):
            return (ListNode(""))
        nodeList.sort()
        currentNode = dummyNode = ListNode(0)
        for j in nodeList:
            currentNode.next = ListNode(j)
            currentNode = currentNode.next
        return dummyNode.next
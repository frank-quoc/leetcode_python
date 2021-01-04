# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize the head and tail values to -1
        head = tail = ListNode(-1)
        while l1 and l2: # while there are still values in the two nodes
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        # Any left overs are added
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return head.next

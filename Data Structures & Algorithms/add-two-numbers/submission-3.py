# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryover = 0
        curr = None
        head = None
        while l1 and l2:
            summary = l1.val + l2.val + carryover
            if summary > 9:
                carryover=1
                summary -=10
            else:
                carryover = 0

            if not curr:
                curr = ListNode(summary)
                head = curr

            else:

                curr.next = ListNode(summary)
                curr = curr.next
            l1 = l1.next
            l2 = l2.next

        leftover= None
        if l1: leftover = l1
        elif l2: leftover = l2

        while leftover:
            summary = leftover.val + carryover
            if summary > 9:
                carryover=1
                summary -=10
            else:
                carryover = 0
            curr.next = ListNode(summary)
            curr = curr.next
            leftover = leftover.next
        if carryover > 0:
            curr.next = ListNode(carryover)
        return head
            
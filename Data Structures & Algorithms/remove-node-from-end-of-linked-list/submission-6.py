# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        curr = head
        index = 0
        prev = None
        while index < size - n:
            index +=1
            prev = curr
            curr = curr.next
        if size - n == 0:
            return head.next
        prev.next = prev.next.next

        return head
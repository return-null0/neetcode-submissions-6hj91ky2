# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the list in half. get two head pointers
        #reverse the second half and merge

        slow = head
        fast = head

        if not slow.next:
            return
            
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None


        prev = fast
        fast = fast.next
        prev.next = None
        while fast:
            temp = fast.next
            fast.next = prev
            prev = fast
            fast = temp

        head2 = prev
        curr1 = head.next
        curr2 = head2
        merged = head
        
        while curr1 and curr2:
            merged.next = curr2
            curr2 = curr2.next
            merged.next.next = curr1
            curr1 = curr1.next
            merged = merged.next.next
        return


        
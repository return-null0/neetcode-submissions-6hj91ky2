# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2: 
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        else:
            merged = ListNode()
            head = merged
            while list1 and list2:
                if list1.val<= list2.val:
                    merged.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    merged.next = ListNode(list2.val)
                    list2 = list2.next
                merged = merged.next

            leftover = None
            if list1: leftover = list1
            if list2: leftover = list2 
            while leftover: 
                merged.next = ListNode(leftover.val)
                leftover = leftover.next
                merged = merged.next
            return head.next

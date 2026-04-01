"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        ogToNewMap = {None : None}
        while current:
            ogToNewMap[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            ogToNewMap[current].next = ogToNewMap[current.next]
            ogToNewMap[current].random = ogToNewMap[current.random]
            current = current.next
            
        return ogToNewMap[head]

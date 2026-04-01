# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        navStack = []
        curr = root

        while curr or len(navStack) > 0:
            while curr:
                navStack.append(curr)
                curr = curr.left
            node = navStack.pop()
            k -=1
            if k == 0:
                return node.val 
            curr=node.right


        
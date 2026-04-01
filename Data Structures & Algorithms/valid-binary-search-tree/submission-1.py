# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    validBounds = [float("-inf"), float("inf")]
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if root.val <= self.validBounds[0] or root.val >= self.validBounds[1]:
            return False

        prevLeast , prevGreatest = self.validBounds[0], self.validBounds[1]

        self.validBounds[1] = root.val
        left = self.isValidBST(root.left)
        self.validBounds[1] = prevGreatest

        self.validBounds[0] = root.val
        right = self.isValidBST(root.right)
        self.validBounds[0] = prevLeast

        return left and right
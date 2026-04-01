# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) < 1: return None
        currVal = preorder[0]

        mid = inorder.index(currVal)
        currNode = TreeNode(currVal)
        currNode.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        currNode.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return currNode
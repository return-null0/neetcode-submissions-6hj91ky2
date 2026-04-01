# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #search  if the nodes are the same do tree comparison

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val == subRoot.val:
            return self.equalTrees(root,subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def equalTrees(self, p, q):
        if not p and q or p and not q:
            return False
        if not p and not q:
            return True
        if p.val==q.val:
            return self.equalTrees(p.left, q.left) and self.equalTrees(p.right, q.right)
        else:
            return False
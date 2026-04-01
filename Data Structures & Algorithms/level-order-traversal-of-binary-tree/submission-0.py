# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if root is None: return []
        ans = []
        q.appendleft(root)
        while q:
            size = len(q)
            currLevel = []
            for i in range(size):
                node = q.popleft()
                currLevel.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(currLevel)
        return ans
            
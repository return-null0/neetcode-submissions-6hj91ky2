class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        max_diameter = 0
        
        def dfs(node):
            if not node:
                return 0
                
            # This keyword disables the scoping trap
            nonlocal max_diameter
                
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            local_diameter = left_depth + right_depth
            
            # This now updates the outer variable flawlessly
            max_diameter = max(max_diameter, local_diameter)
            
            return 1 + max(left_depth, right_depth)
            
        dfs(root)
        return max_diameter
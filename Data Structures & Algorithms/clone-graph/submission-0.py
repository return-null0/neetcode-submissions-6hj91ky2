class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        oldToNew = {}
        
        def cloneDFS(current_node):
            if current_node in oldToNew:
                return oldToNew[current_node]
            
            oldToNew[current_node] = Node(current_node.val)
            
            for neighbor in current_node.neighbors:
                oldToNew[current_node].neighbors.append(cloneDFS(neighbor))
            
            return oldToNew[current_node]
            
        return cloneDFS(node)
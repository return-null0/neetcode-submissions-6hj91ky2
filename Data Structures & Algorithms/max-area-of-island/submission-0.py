class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid=grid
        maximum = 0
        visited = set()
    
        def maximizeIsland(x,y):
            if y < 0 or y > len(self.grid) - 1 or x < 0 or x > len(self.grid[y]) - 1:
                return 0
                nonlocal visited
            if (x,y) in visited: return 0
            if self.grid[y][x] == 0:
                return 0
            visited.add((x,y))
            
            return maximizeIsland(x-1,y) + maximizeIsland(x+1,y) + maximizeIsland(x,y-1) + maximizeIsland(x, y+1) + 1

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    curr = maximizeIsland(x,y)
                    if curr > maximum: maximum = curr
        return maximum
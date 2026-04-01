class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # routine -> search for potential island (1)
        # mark visited 
        # search neighbors of potential islands to expand island

        visited = []
        ans = 0
        for i in grid:
            visited.append(len(i) * [0])

        for i, ele1 in enumerate(grid):
            for j in range(len(ele1)):
                if visited[i][j]:
                    continue
                if ele1[j] == "0":
                    visited[i][j] = 1
                else:
                    ans +=1
                    self.islandSearch(grid, visited,i, j)
        return ans
    

    def islandSearch(self,grid, visited, i, j):

        if i < 0 or i > len(visited) - 1:
            return
        if j < 0 or j > len(visited[0]) - 1:
            return

        if visited[i][j] or grid[i][j]=="0":
            return 

            
        visited[i][j] = 1
        self.islandSearch(grid, visited, i-1, j )
        self.islandSearch(grid, visited, i+1, j )
        self.islandSearch(grid, visited, i, j-1)
        self.islandSearch(grid, visited, i, j+1)

            
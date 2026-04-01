class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # directed graph

        visiting = set()
        adjList = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjList[crs].append(pre)


        # completion is satisfied
        def dfs(index):
        # build adjacency list
            if adjList[index] == []:
                return True
            if index in visiting:
                return False
            
            visiting.add(index)
            neighbors = adjList[index]
            for neighbor in neighbors:
                if dfs(neighbor) == False:
                    return False
            visiting.remove(index)
            adjList[index] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
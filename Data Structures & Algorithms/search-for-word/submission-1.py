class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        candidates = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    candidates.append([i,j])
        visited = set()
        def recurse(i,j, index):
            if not i < len(board) or i < 0 or not j < len(board[i]) or j < 0:
                return False
            if (i,j) in visited:
                return False
            if index == len(word) - 1 and word[index] == board[i][j]:
                return True
            if board[i][j] != word[index]:
                return False
            if index < len(word) - 1 and word[index]==board[i][j]:
                visited.add((i,j))
                found = recurse(i-1, j, index+1) or recurse(i+1,j, index+1) or recurse(i, j-1, index + 1) or recurse(i,j+1, index+1)
                visited.remove((i,j))
                return found
        ans = False
        for z in range(len(candidates)):
            ans = ans or recurse(candidates[z][0], candidates[z][1], 0)
        return ans
            
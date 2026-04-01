class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for r in range(9):
            seen = set()
            for c in range(9):
                v = board[r][c]
                if v == '.': 
                    continue
                if v in seen: 
                    return False
                seen.add(v)

        # columns
        for c in range(9):
            seen = set()
            for r in range(9):
                v = board[r][c]
                if v == '.': 
                    continue
                if v in seen: 
                    return False
                seen.add(v)

        # 3x3 boxes
        for i in range(3):              # box row index: 0,1,2
            for j in range(3):          # box col index: 0,1,2
                seen = set()
                y = i * 3               # top-left row of this box
                x = j * 3               # top-left col of this box
                for z in range(9):
                    v = board[y][x]
                    if v != '.':
                        if v in seen:
                            return False
                        seen.add(v)

                    # move right; wrap to next row after 3 cells
                    x += 1
                    if (z + 1) % 3 == 0:
                        x = j * 3
                        y += 1

        return True
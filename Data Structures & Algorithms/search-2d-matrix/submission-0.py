class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        verticalStart = 0
        verticalEnd = len(matrix) -1

        #find row first
        row = -1
        while verticalStart <= verticalEnd:
            mid = (verticalStart + verticalEnd) // 2
            if matrix[mid][0] > target:
                verticalEnd = mid - 1
            elif matrix[mid][len(matrix[mid])-1] < target:
                verticalStart = mid + 1
            else:
                row = mid
                break
        
        if row == -1: return False

        start = 0
        end = len(matrix[row]) - 1
        while start <= end:
            mid = (start + end) // 2
            if matrix[row][mid] < target: 
                start = mid + 1
            elif matrix[row][mid] > target:
                end = mid - 1
            else:
                return True
        
        return False
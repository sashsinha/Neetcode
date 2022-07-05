class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row = 0
        col = n - 1
        while row < m and col >= 0:
            val = matrix[row][col]
            if val < target:
                row += 1
            elif val > target:
                col -= 1
            else:
                return True        
        return False

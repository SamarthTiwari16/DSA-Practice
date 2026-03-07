matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5 # Output: true

# TC=O(log(n+m)) SC=O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) # rows
        m = len(matrix[0]) # columns
        row = 0
        col = m-1
        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1  # Move down
            else:
                col -= 1 # Move left
        return False

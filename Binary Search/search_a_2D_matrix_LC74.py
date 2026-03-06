# Approach 1: TC=O(logn+logm)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        # BS for searching row
        l = 0
        h = n-1
        while l <= h:
            mid = (l+h)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid+1
            else:
                h = mid-1
        row = h
        if row < 0:
            return False
        # BS on unique row
        l = 0
        h = m-1
        while l <= h:
            mid = (l+h)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid+1
            else:
                h = mid-1
        return False

# Approach 2: TC=O(log(n×m))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) # rows
        m = len(matrix[0]) # columns
        left = 0
        right = (m*n)-1
        while left <= right:
            mid = (left+right)//2
            row = mid//m
            col = mid%m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid+1
            else:
                right = mid-1
        return False

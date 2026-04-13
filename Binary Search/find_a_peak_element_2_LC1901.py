mat = [[1,4],[3,2]]   # Output: [0,1]

# TC = O(nlogm)
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)  #row
        m = len(mat[0])  #col
        low = 0
        high = m - 1
        while low <= high:
            mid = (low+high)//2
            max_row = 0
            for i in range(n):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i
            if mid > 0:
                left_value = mat[max_row][mid-1]
            else:
                left_value = -1
            if mid < m-1:
                right_value = mat[max_row][mid+1]
            else:
                right_value = -1
            current = mat[max_row][mid]
            if current > left_value and current > right_value:
                return [max_row, mid]
            elif left_value > current:
                high = mid-1
            else:
                low = mid+1
        return [-1, -1]

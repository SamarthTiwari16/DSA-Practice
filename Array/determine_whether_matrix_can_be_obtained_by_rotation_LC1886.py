mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]   # Output: true

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate_90_clockwise(matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(i+1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            for row in matrix:
                row.reverse()
        for i in range(4):  # 4 orientations: 0, 90, 180, 360
            if mat == target:
                return True
            rotate_90_clockwise(mat)
        return False

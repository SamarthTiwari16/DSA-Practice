n = 3 # Output: [[1,2,3],[8,9,4],[7,6,5]]

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for i in range(n)]
        num = 1 #counter starting from 1 
        r = n #rows
        c = n #columns
        left = 0
        right = c-1
        top = 0
        bottom = r-1
        while top<=bottom and left<=right:
            for i in range(left, right+1):
                matrix[top][i] = num
                num+=1
            top+=1
            for i in range(top, bottom+1):
                matrix[i][right] = num
                num+=1
            right-=1
            if top<=bottom:
                for i in range(right, left-1, -1):
                    matrix[bottom][i] = num
                    num+=1
                bottom-=1
            if left<=right:
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = num
                    num+=1
                left+=1
        return matrix

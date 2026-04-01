# TC=O(logN) SC=O(logN) 
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def solve(n):
            if n == 1:
                return True
            if n<=0 or n%2!=0:
                return False
            return solve(n//2)
        return solve(n)

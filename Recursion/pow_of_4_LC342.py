class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def solve(n):
            if n == 1:
                return True
            if n<=0 or n%4!=0:
                return False
            return solve(n//4)
        return solve(n)

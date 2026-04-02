class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def solve(n):
            if n == 1:
                return True
            if n<=0 or n%3!=0:
                return False
            return solve(n//3)
        return solve(n)

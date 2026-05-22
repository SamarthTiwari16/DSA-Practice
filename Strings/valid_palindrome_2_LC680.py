class Solution:
    def validPalindrome(self, s: str) -> bool:
        def solve(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        n = len(s)
        left = 0
        right = n-1
        while left < right:
            if s[left] != s[right]:
                return solve(left+1, right) or \
                        solve(left, right-1)
            left += 1
            right -= 1
        return True

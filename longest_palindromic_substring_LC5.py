class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        result = s[0]
        def solve(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1: right]
        for i in range(n):
            odd = solve(i, i)
            if len(odd) > len(result):
                result = odd
            even = solve(i, i+1)
            if len(even) > len(result):
                result = even
        return result

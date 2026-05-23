Input: s = "abc"   #   Output: 3

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        length = 0
        def solve(left, right):
            count = 0
            while left >=0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        for i in range(n):
            odd = solve(i, i)
            length += odd
            even = solve(i, i+1)
            length += even
        return length

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        def solve(left, right):
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            solve(left+1, right-1)
        solve(0, n-1)

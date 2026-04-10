g = [1,2,3], s = [1,1]    # Output: 1


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = len(g)
        m = len(s)
        i = 0
        j = 0
        count = 0
        while i < n and j < m:
            if s[j] >= g[i]:
                count += 1
                i += 1
            j += 1
        return count

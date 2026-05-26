Input: s1 = "ab", s2 = "eidbaooo"    # Output: true

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        s1_map = {}
        window_map = {}
        for ch in s1:
            s1_map[ch] = s1_map.get(ch, 0)+1
        for i in range(n):
            window_map[s2[i]] = window_map.get(s2[i], 0)+1
        if s1_map == window_map:
            return True
        for i in range(n, m):
            window_map[s2[i]] = window_map.get(s2[i], 0)+1
            old_char = s2[i-n]
            window_map[old_char] -= 1
            if window_map[old_char] == 0:
                del window_map[old_char]
            if s1_map == window_map:
                return True
        return False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        n = len(strs)
        for i in range(len(strs[0])):
            ans = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != ans:
                    return strs[0][:i]
        return strs[0]

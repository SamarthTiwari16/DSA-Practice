n = 2    # Output: [0,1,3,2]

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        ans = 0
        for i in range(1 << n):
            res.append(i ^ (i >> 1))
        return res

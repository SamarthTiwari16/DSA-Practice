bloomDay = [1,10,3,10,2], m = 3, k = 1     # Output: 3

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        def solve(mid):
            c_f = 0
            b = 0
            for i in range(n):
                if bloomDay[i] <= mid:
                    c_f += 1
                    if c_f == k:
                        b += 1
                        c_f = 0
                else:
                    c_f = 0
            return b >= m
        left = min(bloomDay)
        right = max(bloomDay)
        while left <= right:
            mid = (left+right)//2
            if solve(mid):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans

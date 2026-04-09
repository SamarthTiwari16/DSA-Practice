bloomDay = [1,10,3,10,2], m = 3, k = 1     # Output: 3

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1
        def solve(mid):
            b = 0 # bouquets
            c = 0 # consecutive
            for i in bloomDay:
                if i <= mid:
                    c += 1
                    if c == k:
                        b += 1
                        c = 0
                else:
                    c = 0
                if b >= m:
                    return True
            return b >= m
                
        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1
        while low <= high:
            mid = (low+high)//2
            if solve(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans

dist = [1,3,2]     # Output: 1
hour = 6

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def solve(k):
            n = len(dist)
            hrs = 0
            for i in range(n-1):
                hrs += (dist[i]+k-1)//k
            hrs += dist[-1]/k
            return hrs <= hour
        if not solve(10**7):
            return -1

        left = 1
        right = 10**7
        while left < right:
            mid = (left+right)//2
            if solve(mid):
                right = mid
            else:
                left = mid+1
        return left

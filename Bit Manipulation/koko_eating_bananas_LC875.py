piles = [3,6,7,11], h = 8     # Output: 4

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def solve(k):
            hours = 0
            for i in piles:
                hours += (i + k - 1) // k
            return hours <= h

        n = max(piles)
        low = 1
        high = n
        while low < high:
            mid = (low + high)//2
            if solve(mid):
                high = mid
            else:
                low = mid+1
        return low

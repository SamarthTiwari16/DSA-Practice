weights = [1,2,3,4,5,6,7,8,9,10]       # Output: 15
days = 5

# TC=O(NlogM)
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        def solve(mid):
            day = 1
            curr = 0
            for i in weights:
                if curr + i > mid:
                    day += 1
                    curr = i
                else:
                    curr += i
                if day > days:
                    return False
            return day <= days

        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = (low+high)//2
            if solve(mid):
                high = mid
            else:
                low = mid + 1
        return low

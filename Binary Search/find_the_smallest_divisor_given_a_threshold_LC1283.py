nums = [1,2,5,9]     # Output: 5
threshold = 6

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def solve(mid):
            sumi = 0
            for i in nums:
                sumi += (i + mid - 1)//mid
            if sumi <= threshold:
                return True
            return False

        low = 1
        high = max(nums)
        while low < high:
            mid = (low+high)//2
            if solve(mid):
                high = mid
            else:
                low = mid+1
        return low

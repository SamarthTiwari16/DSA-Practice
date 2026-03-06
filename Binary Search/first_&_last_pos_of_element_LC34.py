nums = [5,7,7,8,8,10], target = 8  # Output: [3, 4]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        n = len(nums)
        left = 0
        right = n-1
        lb = n
        while left <= right:
            mid = (left+right)//2
            if nums[mid] >= target:
                lb = mid
                right = mid-1
            else:
                left = mid+1
        ub = n
        left = 0
        right = n-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > target:
                ub = mid
                right = mid-1
            else:
                left = mid+1
        return [lb, ub-1]

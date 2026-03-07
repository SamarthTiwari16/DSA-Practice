nums = [3,4,5,1,2]  # Output: 1

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        h = n-1
        while l < h:
            mid = (l+h)//2
            if nums[mid] > nums[h]:
                l = mid+1
            else:
                h = mid
        return nums[l]

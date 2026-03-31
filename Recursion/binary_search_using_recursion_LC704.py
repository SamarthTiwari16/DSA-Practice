class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        def bs(left, right):
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return -1
        return bs(left, right)

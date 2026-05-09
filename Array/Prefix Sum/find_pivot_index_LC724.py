nums = [1,7,3,6,5,6]    # Output: 3

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = 0
        for i in range(n):
            totalSum += nums[i]
        leftSum = 0
        for j in range(n):
            rightSum = totalSum - leftSum - nums[j]
            if leftSum == rightSum:
                return j
            leftSum += nums[j]
        return -1

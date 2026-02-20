nums = [4,1,2,1,2]

# TC=O(N), SC=O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n==1:
            return nums[-1]
        for i in range(0, n-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]

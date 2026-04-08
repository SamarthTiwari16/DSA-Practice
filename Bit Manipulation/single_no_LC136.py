nums = [4,1,2,1,2] # Output: 4

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans = i ^ ans
        return ans

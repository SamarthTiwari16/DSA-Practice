nums = [1,1,1], k = 2     # Output: 2

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        pre_sum = 0
        freq = {0:1} 
        for i in range(n):
            pre_sum += nums[i]
            if (pre_sum - k) in freq:
                count += freq[pre_sum - k]
            freq[pre_sum] = freq.get(pre_sum, 0) + 1
        return count

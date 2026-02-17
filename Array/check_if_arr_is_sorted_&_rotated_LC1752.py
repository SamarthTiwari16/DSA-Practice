nums = [3,4,5,1,2]

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        drop = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                drop+=1
        if nums[n-1] > nums[0]:
            drop+=1
        return drop<=1

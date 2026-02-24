# Optimal solution TC=O(N) SC=O(N)
result = [0]*n
pos, neg = 0, 1
for i in range(0, n):
    if nums[i] >= 0:
        result[pos] = nums[i]
        pos += 2
    else:
        result[neg] = nums[i]
        neg += 2
print(result)

# In-place (Failed in some testcases, but correct and efficient for space)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = 1
        while i < n and j < n:
            while i < n and nums[i] > 0:
                i += 2
            while j < n and nums[j] < 0:
                j += 2
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]
        return nums

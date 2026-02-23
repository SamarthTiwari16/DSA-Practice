nums = [0,2,1,5,3,4] # Output: [0,1,2,4,5,3]


# TC=O(N) SC=O(N)
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []*n
        for i in range(n):
            ans.append(nums[nums[i]])
        return ans

# TC=O(N) SC=O(1)
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            ori = nums[i] % n
            target = nums[ori] % n
            nums[i] = nums[i]+n*target
        for i in range(n):
            nums[i] = nums[i]//n
        return nums

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        m = len(nums)
        ans = [0]*m
        j = n
        i = 0
        p = 0
        while p<m:
            ans[p] = nums[i]
            i+=1
            p+=1
            ans[p] = nums[j]
            j+=1
            p+=1
        return ans

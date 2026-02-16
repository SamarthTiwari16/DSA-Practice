nums = [1,2,3,4,3]

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        stack = []
        for i in range(2*n-1, -1, -1):
            while len(stack)!=0 and nums[stack[-1]]<=nums[i%n]:
                stack.pop()
            if i<n:
                if len(stack)!=0:
                    ans[i]=nums[stack[-1]]
            stack.append(i%n)
        return ans

# Here we are using nums[stack] cozz stack stores postions, not values. Here we want to store values. So store it from nums we apply nums[stack], it stores values, not positions. 

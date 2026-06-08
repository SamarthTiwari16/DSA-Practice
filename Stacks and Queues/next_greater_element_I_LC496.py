nums1 = [4,1,2], nums2 = [1,3,4,2]     # Output: [-1,3,-1]

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        stack = []
        n_g = {}
        for i in range(m-1, -1, -1):
            elem = nums2[i]
            while stack and stack[-1] <= elem:
                stack.pop()
            if stack:
                n_g[elem] = stack[-1]
            else:
                n_g[elem] = -1
            stack.append(elem)
        result = []
        for i in nums1:
            result.append(n_g[i])
        return result

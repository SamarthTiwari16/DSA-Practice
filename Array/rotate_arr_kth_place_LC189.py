class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()  # Part1
        n = len(nums)
        k = k % n
        start = 0  # Part2
        end = k-1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        start = k  # Part3
        end = n-1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

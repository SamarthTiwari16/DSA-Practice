# Recursive Solution TC=O(logn) SC=O(1)

nums = [2, 4, 6, 7, 9, 11, 18, 19]
target = 9
low = 0
high = len(nums) - 1
def binary_search(nums, low, high, target):
    if low > high: return -1
    mid = (low+high)//2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search(nums, mid+1, high, target)
    else:
        return binary_search(nums, low, mid-1, target)
print(binary_search(nums, low, high, target))

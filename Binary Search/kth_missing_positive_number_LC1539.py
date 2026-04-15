arr = [2,3,4,7,11]   # Output: 9
k = 5

# TC=O(logN) SC=O(1)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        low = 0
        high = n-1
        while low <= high:
            mid = (low+high)//2
            missing = arr[mid]-(mid+1)
            if missing < k:
                low = mid+1
            else:
                high = mid-1
        return low + k

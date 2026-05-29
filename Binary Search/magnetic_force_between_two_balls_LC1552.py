position = [1,2,3,4,7], m = 3     # Output: 3

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        def solve(mid):
            count = 1
            last_pos  = position[0]
            for i in range(1,n):
                if position[i] - last_pos >= mid:
                    count += 1
                    last_pos = position[i]
            if count >= m:
                return True
            else:
                return False
        left = 1
        right = position[-1] - position[0]
        ans = 1
        while left <= right:
            mid = (left+right)//2
            if solve(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        return ans

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = []
        def solve(index, total, subset):
            if total == target:
                result.append(subset.copy())
                return
            elif total > target:
                return
            if index >= n:
                return
            sum = total + candidates[index]
            subset.append(candidates[index])
            solve(index, sum, subset)
            subset.pop()
            solve(index+1, total, subset)
        solve(0, 0, [])
        return result

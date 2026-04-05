# Brute Force
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        my_set = set()
        def solve(index, total, subset):
            if total == target:
                my_set.add(tuple(subset))
                return
            elif total > target:
                return
            if index >= n:
                return
            subset.append(candidates[index])
            sum = total + candidates[index]
            solve(index+1, sum, subset)
            subset.pop()
            next_index = index + 1
            while next_index < n and candidates[next_index] == candidates[index]:
                next_index += 1
            solve(next_index, total, subset)
        solve(0, 0, [])
        return list(my_set)

# Optimal
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
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
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                sum = total + candidates[i]
                solve(i+1, sum, subset)
                subset.pop()
        solve(0, 0, [])
        return result
